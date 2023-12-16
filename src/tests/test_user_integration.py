import pytest
from faker import Faker

from src.data.use_cases import UserDelete, UserFinder, UserRegister
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
    user_finder = UserRegister(user_repository)
    response = user_finder.create(
        first_name=data["name"],
        last_name=data["last_name"],
        age=data["age"],
    )

    assert response is None


def test_find_user(data):
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    response = user_finder.find(data["name"])
    assert response["attributes"]["first_name"] == data["name"]
    assert response["attributes"]["last_name"] == data["last_name"]
    assert response["attributes"]["age"] == data["age"]


def test_delete_user():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserDelete(user_repository)
    user = user_finder.delete(user_id=1)
    assert user is None
