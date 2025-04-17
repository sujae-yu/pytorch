from typing import Any, Union

from torch._inductor.ir import ComputedBuffer, InputBuffer
from torch.utils._ordered_set import OrderedSet

from ..cutlass_utils import try_import_cutlass


EpilogueFunctor = Any  # EpilogueFunctor local class defined in _trace
Buffer = Union[ComputedBuffer, InputBuffer]
CutlassTupleType = Any  # cutlass.backend.c_types.tuple_factory_.<locals>.TupleType
CutlassVisitorType = Any  # cutlass.backend.c_types.visitor_factory.<locals>.VisitorType
CutlassArgType = (
    Any  # Can be a CutlassTupleType, CutlassVisitorType, EmptyByte, or ctype.c_void_p
)


if try_import_cutlass():
    import ast
    import ctypes
    import textwrap

    from cutlass.backend.c_types import (  # type: ignore[import-untyped, import-not-found]
        EmptyByte,
    )
    from cutlass.backend.epilogue import (  # type: ignore[import-untyped, import-not-found]
        dtype2ctype,
    )
    from cutlass.backend.evt import (  # type: ignore[import-untyped, import-not-found]
        EpilogueFunctorVisitor,
    )
    from cutlass.backend.evt.backend.emitter_base import (  # type: ignore[import-untyped, import-not-found]
        FusionCallbacks,
    )
    from cutlass.backend.evt.backend.sm90_emitter import (  # type: ignore[import-untyped, import-not-found]
        CollectiveEpilogue,
    )
    from cutlass.backend.evt.frontend import (  # type: ignore[import-untyped, import-not-found]
        PythonASTFrontend,
    )
    from cutlass.backend.evt.ir.tensor import (  # type: ignore[import-untyped, import-not-found]
        Tensor as CutlassTensor,
    )
    from cutlass_library import DataType, EpilogueScheduleType, TileDescription

    from torch._inductor.codegen.cuda import cuda_env
    from torch._inductor.utils import IndentedBuffer

    _CUTLASS_C_DTYPES = OrderedSet(dtype2ctype.values())  # type: ignore[var-annotated]

    def trace(
        fn_src: str,
        example_tensors: dict[str, CutlassTensor],
        accum_type: DataType,
        output_type: DataType,
        tile_description: TileDescription,
        epilogue_schedule: EpilogueScheduleType,
        **kwargs: dict[str, Any],
    ) -> tuple[str, str]:
        cuda_arch = int(cuda_env.get_cuda_arch())  # type: ignore[arg-type]
        assert cuda_arch >= 90, "Only SM90+ is supported for EVT"
        epilogue_functor = _trace(fn_src, example_tensors, **kwargs)
        visitor = EpilogueFunctorVisitor(cuda_arch, epilogue_functor)
        fusion_callbacks = FusionCallbacks(visitor.graph, cuda_arch, emit_CD=False)
        collective_epilogue = CollectiveEpilogue(
            tile_description,
            epilogue_schedule,
            accum_type,
            output_type,
            fusion_callbacks,
        )

        return collective_epilogue.emit()

    # Based off of
    # https://github.com/NVIDIA/cutlass/blob/df18f5e4f5de76bed8be1de8e4c245f2f5ec3020/python/cutlass/epilogue/epilogue.py#L117
    # This is modified to enable directly passing the source code of the epilogue vs getting it from a bona-fide python function
    # The reason for this is that inspect.getsource does not work with functions defined at runtime via exec/eval
    def _trace(
        fn_src: str, example_tensors: dict[str, CutlassTensor], **kwargs: Any
    ) -> EpilogueFunctor:
        class EpilogueFunctor(PythonASTFrontend):
            def __init__(self, **kwargs: dict[str, Any]):
                self.source = textwrap.dedent(fn_src)
                super().__init__(**kwargs)

            def parse(self, example_inputs: dict[str, CutlassTensor]) -> None:
                self.example_inputs = example_inputs
                self.ast = ast.parse(self.source)
                self.visit(self.ast)

        epilogue_functor = EpilogueFunctor(**kwargs)
        epilogue_functor.trace(example_tensors)
        return epilogue_functor

    def _render_argument_type(
        epilogue_functor: EpilogueFunctor,
        name_to_buffer: dict[str, Buffer],
    ) -> str:
        epilogue_thread_type = epilogue_functor.epilogue_thread_type

        # Fragile, but this is the only way to guarantee t is expected type because t is a local class
        def is_nested_visitor_type(t: type) -> bool:
            return (
                ".".join([t.__module__, t.__qualname__])
                == "cutlass.backend.c_types.visitor_factory.<locals>.VisitorType"
            )

        buffer = IndentedBuffer()

        def render_argument_type(name: str, t: CutlassArgType) -> None:
            if issubclass(t, ctypes.c_byte):
                buffer.writeline(f"{{}}, /* {name} */")
            else:
                fields = [
                    (fname, _get_arg_from_node(ty, name_to_buffer[name]))
                    for fname, ty in t._fields_
                ]
                field_strs = [f"/* {fname} */ {str(field)}" for fname, field in fields]
                buffer.writeline(f"{{{', '.join(field_strs)}}}, /* {name} */")

        def render_thread_type(name: str, t: CutlassArgType) -> None:
            if is_nested_visitor_type(t):
                buffer.writeline(f"{{ /* {name} */")
                with buffer.indent():
                    for name, inner_t in t._fields_:
                        render_thread_type(name, inner_t)
                buffer.writeline("},")
            else:
                render_argument_type(name, t)

        buffer.writeline("{{")
        with buffer.indent():
            render_thread_type("thread", epilogue_thread_type)

        buffer.writeline("}};")

        return buffer.getvalue()

    def _get_arg_from_node(arg_ty: type, node: Buffer) -> str:
        from ..cuda_template import CUTLASSTemplate

        # Today, arguments are either a pointer to the
        # node's memory, a stride tuple, the datatype
        # Once again, need to check for local class type for stride tuple
        if (
            str(arg_ty)
            == "<class 'cutlass.backend.c_types.tuple_factory_.<locals>.TupleType'>"
        ):
            DEFAULT_STRIDE_LEN = 3
            assert len(node.get_layout().stride) <= DEFAULT_STRIDE_LEN
            stride = [int(x) for x in node.get_layout().stride]
            for _ in range(DEFAULT_STRIDE_LEN - len(stride)):
                stride.append(0)

            def render_stride(x: int) -> str:
                # Handle EBO for 0 and 1
                if x == 0:
                    return "_0{}"
                elif x == 1:
                    return "_1{}"
                else:
                    return str(x)

            return f"{{{', '.join([render_stride(x) for x in stride])}}}"

        elif issubclass(arg_ty, ctypes.c_void_p):
            return f"{node.get_name()}.get()"
        elif (
            arg_ty in _CUTLASS_C_DTYPES
        ):  # Assumption: this is the element dtype, this holds for all cutlass ir nodes currently
            return CUTLASSTemplate._DTYPE_TO_CUTLASS[node.get_layout().dtype]
        elif issubclass(arg_ty, EmptyByte):
            return "{}"

        raise NotImplementedError(f"Unsupported arg type: {arg_ty}")
