def headers_add_host(headers, address):
    """
    If there is no Host field in the headers, insert the address as a Host into the headers.
    A Host field in any letter case, such as 'host', counts.

    :param headers: a 'dict'(header name, header value) of http request headers
    :param address: a string represents a domain name
    :return: headers after adding
    """

    names = {k.lower() for k in headers}
    if "host" not in names:
        headers["Host"] = address

    return headers


def request_add_host(request, address):
    """
    If the request has no headers field, or request['headers'] does not have a Host field, then add address to Host.

    :param request: a dict(request key, request name) of http request
    :param address: a string represents a domain name
    :return: request after adding
    """

    request.setdefault("headers", {})
    headers_add_host(request["headers"], address)

    return request
