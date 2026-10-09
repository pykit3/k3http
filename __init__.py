"""
HTTP/1.1 client

Use this module, we can set timeout, if timeout raise a 'socket.timeout'.
"""

from .client import (
    BadStatusLineError,
    ChunkedSizeError,
    Client,
    HeadersError,
    HttpError,
    LineTooLongError,
    NotConnectedError,
    ResponseNotReadyError,
)
from .util import (
    headers_add_host,
    request_add_host,
)

__all__ = [
    "BadStatusLineError",
    "ChunkedSizeError",
    "Client",
    "HeadersError",
    "HttpError",
    "LineTooLongError",
    "NotConnectedError",
    "ResponseNotReadyError",
    "headers_add_host",
    "request_add_host",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3http")
