import pytest
from faker import Faker

from src.data.use_cases import UserRegister
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

    mock_user_repository.insert_user.return_value = None
    user_finder = UserRegister(mock_user_repository)

    response = user_finder.create(
        first_name=data["name"], last_name=data["last_name"], age=data["age"]
    )

    assert response is None


def test_register_user_with_invalid_first_name():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserRegister(user_repository)
    with pytest.raises(TypeError) as exc_info:
        user_finder.create(first_name=9_090_983, last_name="Silva", age=25)

    assert str(exc_info.value) == "First name must be a string"


def test_register_user_with_invalid_first_name_length():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_register = UserRegister(user_repository)
    with pytest.raises(ValueError) as exc_info:
        user_register.create(first_name="a" * 19, last_name="Silva", age=25)

    assert str(exc_info.value) == "First name must be less than 18 characters"
