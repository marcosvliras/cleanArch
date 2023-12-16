from src.presentation.http_types.http_response import HttpResponse

from .types import *

TYPE_ERROS = [HttpBadRequestError, HttpNotFoundError]


def handle_errors(error: Exception) -> HttpResponse:
    for type_error in TYPE_ERROS:
        if isinstance(error, type_error):
            message = error.message
            name = error.name
            status_code = error.status_code
            return HttpResponse(
                status_code=status_code,
                body={"error": {"message": message, "name": name}},
            )

    return HttpResponse(
        status_code=500,
        body={
            "error": {
                "message": "Internal Server Error",
                "name": "InternalServerError",
            }
        },
    )
