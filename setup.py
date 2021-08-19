# DO NOT EDIT!!! built with `python _building/build_setup.py`
import setuptools
setuptools.setup(
    name="k3http",
    packages=["k3http"],
    version="0.1.0",
    license='MIT',
    description="We find that 'httplib' must work in blocking mode and it can not have a timeout when recving response.Use this module, we can set timeout, if timeout raise a 'socket.timeout'.",
    long_description="# k3http\n\n[![Action-CI](https://github.com/pykit3/k3http/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3http/actions/workflows/python-package.yml)\n[![Build Status](https://travis-ci.com/pykit3/k3http.svg?branch=master)](https://travis-ci.com/pykit3/k3http)\n[![Documentation Status](https://readthedocs.org/projects/k3http/badge/?version=stable)](https://k3http.readthedocs.io/en/stable/?badge=stable)\n[![Package](https://img.shields.io/pypi/pyversions/k3http)](https://pypi.org/project/k3http)\n\nWe find that 'httplib' must work in blocking mode and it can not have a timeout when recving response.Use this module, we can set timeout, if timeout raise a 'socket.timeout'.\n\nk3http is a component of [pykit3] project: a python3 toolkit set.\n\n\nHTTP/1.1 client\nWe find that httplib must work in blocking mode and it can not have a timeout when recving response.\nUse this module, we can set timeout, if timeout raise a socket.timeout.\n\n\n\n# Install\n\n```\npip install k3http\n```\n\n# Synopsis\n\n```python\n\n```\n\n#   Author\n\nZhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n#   Copyright and License\n\nThe MIT License (MIT)\n\nCopyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n\n[pykit3]: https://github.com/pykit3",
    long_description_content_type="text/markdown",
    author='Zhang Yanpo',
    author_email='drdr.xp@gmail.com',
    url='https://github.com/pykit3/k3http',
    keywords=['python', 'http'],
    python_requires='>=3.0',

    install_requires=['k3ut>=0.1.15,<0.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ] + ['Programming Language :: Python :: 3'],
)
