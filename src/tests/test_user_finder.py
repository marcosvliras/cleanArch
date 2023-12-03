import pytest
from faker import Faker

from src.data.use_cases.user_finder import UserFinder
from src.infra.db.entities import User as UserEntity
from src.infra.db.repositories.users_repository import UserRepository

from .connection_test import SessionLocalTestIntegration


@pytest.fixture(scope="session")
def data():
    faker = Faker()
    mocked_first_name = faker.name()
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
    user = user_finder.find(data["name"])
    assert user[0].first_name == data["name"]
    assert user[0].last_name == data["last_name"]
    assert user[0].age == data["age"]


def test_delete_user():
    user_repository = UserRepository(SessionLocalTestIntegration)
    user_finder = UserFinder(user_repository)
    user = user_finder.delete(user_id=1)
    assert user is None
