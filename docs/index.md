# k3http

[![Action-CI](https://github.com/pykit3/k3http/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3http/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3http/badge/?version=stable)](https://k3http.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3http)](https://pypi.org/project/k3http)

HTTP/1.1 client with timeout support. Raises `socket.timeout` when timeout occurs.

k3http is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3http
```

## Quick Start

```python
import k3http
import socket

# Simple GET request
try:
    h = k3http.Client('127.0.0.1', 80)
    h.request('/test.txt', method='GET', headers={'Host': '127.0.0.1'})

    print(h.status)   # 200, 404, etc.
    print(h.headers)  # {'Content-Type': '...', ...}
    print(h.read_body(None))  # response body
except (socket.error, k3http.HttpError) as e:
    print(repr(e))

# POST request with body
content = b'foo=bar'
headers = {
    'Host': 'www.example.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': len(content),
}

try:
    h = k3http.Client('127.0.0.1', 80)
    h.send_request('/api', method='POST', headers=headers)
    h.send_body(content)
    status, headers = h.read_response()
    print(h.read_body(None))
except (socket.error, k3http.HttpError) as e:
    print(repr(e))
```

## API Reference

::: k3http

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
