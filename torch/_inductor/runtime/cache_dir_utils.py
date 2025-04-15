import getpass
import os
import re
import tempfile
from collections.abc import Generator
from contextlib import contextmanager


# Factoring out to file without torch dependencies


def cache_dir() -> str:
    cache_dir = os.environ.get("TORCHINDUCTOR_CACHE_DIR")
    if cache_dir is None:
        os.environ["TORCHINDUCTOR_CACHE_DIR"] = cache_dir = default_cache_dir()
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir


def default_cache_dir() -> str:
    sanitized_username = re.sub(r'[\\/:*?"<>|]', "_", getpass.getuser())
    return os.path.join(
        tempfile.gettempdir(),
        "torchinductor_" + sanitized_username,
    )


def triton_cache_dir(device: int) -> str:
    if (directory := os.getenv("TRITON_CACHE_DIR")) is not None:
        return directory
    return os.path.join(
        cache_dir(),
        "triton",
        str(device),
    )


@contextmanager
def temporary_cache_dir(directory: str) -> Generator[None, None, None]:
    original = os.environ.get("TORCHINDUCTOR_CACHE_DIR")
    os.environ["TORCHINDUCTOR_CACHE_DIR"] = directory
    try:
        yield
    finally:
        if original is None:
            del os.environ["TORCHINDUCTOR_CACHE_DIR"]
        else:
            os.environ["TORCHINDUCTOR_CACHE_DIR"] = original
