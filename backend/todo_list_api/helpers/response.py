import json
from flask import jsonify


def make_response(
        data: str or dict = None,
        error: list or dict = None,
        status_code: int = None
) -> json:

    response = jsonify({
        'data': data,
        'errors': error
    })
    response.status_code = status_code
    return response
