import pytest
from faker import Faker

from src.data.use_cases.user_finder import UserFinder
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


def test_create_user(data):
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    user = user_finder.create(
        first_name=data["name"],
        last_name=data["last_name"],
        age=data["age"],
    )

    assert isinstance(user, UserEntity)


def test_find_user(data):
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    response = user_finder.find(data["name"])
    assert response["attributes"][0].first_name == data["name"]
    assert response["attributes"][0].last_name == data["last_name"]
    assert response["attributes"][0].age == data["age"]


def test_find_user_with_invalid_first_name():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(TypeError) as exc_info:
        user_finder.find(first_name=9_090_983)

    assert str(exc_info.value) == "First name must be a string"


def test_find_user_with_invalid_first_name_length():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(ValueError) as exc_info:
        user_finder.find(first_name="a" * 19)

    assert str(exc_info.value) == "First name must be less than 18 characters"


def test_find_user_with_user_not_found():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    with pytest.raises(ValueError) as exc_info:
        user_finder.find(first_name="JONH DOE")

    assert str(exc_info.value) == "User not found"


def test_delete_user():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    user = user_finder.delete(user_id=1)
    assert user is None
