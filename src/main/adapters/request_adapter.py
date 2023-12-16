from typing import Callable

from flask import request as FlaskRequest

from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


def request_adapter(
    request: FlaskRequest, controller: Callable
) -> HttpResponse:
    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        query_params=request.args,
        path_params=request.view_args,
        body=body,
        headers=request.headers,
        url=request.full_path,
    )

    return controller(http_request)
