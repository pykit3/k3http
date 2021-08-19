"""
HTTP/1.1 client
We find that httplib must work in blocking mode and it can not have a timeout when recving response.
Use this module, we can set timeout, if timeout raise a socket.timeout.
"""

# from .proc import CalledProcessError
# from .proc import ProcError

__version__ = "0.1.0"
__name__ = "k3http"

from .client import (
    HttpError,
    LineTooLongError,
    ChunkedSizeError,
    NotConnectedError,
    ResponseNotReadyError,
    HeadersError,
    BadStatusLineError,
    Client,

)

from .util import(
    headers_add_host,
    request_add_host,
)

__all__ = [
    'HttpError',
    'LineTooLongError',
    'ChunkedSizeError',
    'NotConnectedError',
    'ResponseNotReadyError',
    'HeadersError',
    'BadStatusLineError',
    'Client',

    'headers_add_host',
    'request_add_host',
]

