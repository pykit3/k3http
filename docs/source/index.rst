.. k3http documentation master file, created by
   sphinx-quickstart on Thu May 14 16:58:55 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

k3http
============

.. automodule:: k3http

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. contents::
   :depth: 4
   :local:

Documentation for the Code
**************************

Exceptions
----------

.. autoexception::  HttpError
.. autoexception::  LineTooLongError
.. autoexception::  ChunkedSizeError
.. autoexception::  NotConnectedError
.. autoexception::  ResponseNotReadyError
.. autoexception::  HeadersError
.. autoexception::  BadStatusLineError


Classes
----------

.. autoclass::  Client


Functions
---------

.. autofunction::  headers_add_host
.. autofunction::  request_add_host


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
