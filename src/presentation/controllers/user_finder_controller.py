from src.domain.use_cases.user_finder import UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import \
    ControllerInterface


class UserFinderController(ControllerInterface):
    def __init__(self, user_finder_use_case: UserFinderInterface) -> None:
        self.__user_finder_use_case = user_finder_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]

        response = self.__user_finder_use_case.find(first_name)

        return HttpResponse(status_code=200, body={"data": response})
