from collections import defaultdict

import torch
from torch._inductor.codegen.cuda.cuda_env import get_cuda_arch


PRESETS: dict[int, dict[str, list[str]]] = {}

PRESETS[0] = defaultdict(list)
if torch._C._has_cuda:
    arch = get_cuda_arch()
    if arch == "90":
        preset = PRESETS[0]
        preset["0"] = [
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_64x256x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
        ]
        preset["1111"] = [
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
        ]
        preset["2222"] = [
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x1x1_0_.*_align.*",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
        ]
        preset["3333"] = [
            r"cutlass3x_sm90_tensorop_s64x48x16gemm_.*_64x48x64_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x4x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_4x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_4x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_2x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_4x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x4x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x192x16gemm_.*_256x192x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_2x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x192x16gemm_.*_256x192x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
        ]
        preset["4444"] = [
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_1x8x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_2x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x128_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x160x16gemm_.*_256x160x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x192x16gemm_.*_64x192x64_4x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x160x16gemm_.*_256x160x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x160x16gemm_.*_256x160x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x128_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_2x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_4x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_2x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_2x4x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
        ]
        preset["5555"] = [
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_2x4x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x32x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_128x32x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x256_1x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_1x4x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_2x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x160x16gemm_.*_256x160x64_1x2x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_1x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_256x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x128_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_1x8x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x64x128_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x128_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_64x32x64_1x4x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x192x16gemm_.*_128x192x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x128_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x64_1x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x1x1_0_.*_align.*_cpasync_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_2x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x2x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x64_2x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_2x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x256x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_64x128x128_4x1x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x256x64_1x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x128x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x32x16gemm_.*_128x64x64_1x2x1_0_.*_align.*_warpspecialized_pingpong_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x64x16gemm_.*_128x128x64_2x1x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x128_1x8x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x160x16gemm_.*_256x160x64_1x1x1_0_.*_align.*_stream_k_warpspecialized_cooperative_epi_tma",
            r"cutlass3x_sm90_tensorop_s64x16x16gemm_.*_64x16x256_1x1x1_0_.*_align.*_warpspecialized_epi_nosmem",
            r"cutlass3x_sm90_tensorop_s64x192x16gemm_.*_256x192x64_1x2x1_0_.*_align.*_warpspecialized_cooperative_epi_tma",
        ]
