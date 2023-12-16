import pytest
from faker import Faker

from src.data.use_cases import UserFinder
from src.errors.types import *
from src.infra.db.entities import User as UserEntity
from src.infra.db.repositories.users_repository import UserRepository

from .connection_test import SessionLocalTestIntegration


@pytest.fixture(scope="session")
def data():
    faker = Faker()
    mocked_first_name = faker.pystr_format(string_format=f"{{name}}".ljust(17))
    mocked_last_name = faker.name()
    mocked_age = faker.random_number(digits=2)

    return {
        "name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age,
    }


def test_find_user(mocker, data):
    mock_user_repository = mocker.Mock(
        UserRepository(SessionLocalTestIntegration)
    )

    user_mock = UserEntity(
        first_name=data["name"], last_name=data["last_name"], age=data["age"]
    )
    mock_user_repository.select_user.return_value = [user_mock]
    user_finder = UserFinder(mock_user_repository)

    response = user_finder.find(data["name"])
    print(response)
    assert response["attributes"]["first_name"] == data["name"]
    assert response["attributes"]["last_name"] == data["last_name"]
    assert response["attributes"]["age"] == data["age"]


def test_find_user_with_invalid_first_name():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(HttpBadRequestError) as exc_info:
        user_finder.find(first_name=9_090_983)

    assert str(exc_info.value) == "First name must be a string"


def test_find_user_with_invalid_first_name_length():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(HttpBadRequestError) as exc_info:
        user_finder.find(first_name="a" * 19)

    assert str(exc_info.value) == "First name must be less than 18 characters"


def test_find_user_with_user_not_found():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(HttpNotFoundError) as exc_info:
        user_finder.find(first_name="JONH DOE")

    assert str(exc_info.value) == "User not found"
