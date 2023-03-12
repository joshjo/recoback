def find_header_value(headers, header) -> str | None:
    for key, value in headers:
        if key == header:
            return value.decode("ascii").split()
    return None


def get_token_from_headers(headers) -> str | None:
    header = find_header_value(headers, b"authorization")
    if not header or len(header) < 2:
        return None
    return header[1]
