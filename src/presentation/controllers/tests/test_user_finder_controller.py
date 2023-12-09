import pytest

from src.data.use_cases.user_finder import UserFinder
from src.infra.db.repositories.users_repository import UserRepository
from src.presentation.controllers.user_finder_controller import \
    UserFinderController
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


@pytest.fixture(scope="session")
def data():
    return {
        "type": "Users",
        "count": 1,
        "attributes": [
            {
                "first_name": "Any",
                "last_name": "Any",
                "age": 99,
            }
        ],
    }


def test_handle(mocker, data):
    mock_user_finder = mocker.Mock(UserFinder(UserRepository))
    mock_user_finder.find.return_value = data

    user_finder_controller = UserFinderController(mock_user_finder)

    request = HttpRequest(query_params={"first_name": "Any"})

    response = user_finder_controller.handle(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.status_code == 200
    assert response.body["data"] == data
