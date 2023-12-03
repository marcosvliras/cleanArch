# pylint: disable=R0801

from typing import List

import pytest
from faker import Faker

from src.infra.db.entities import User
from src.infra.db.repositories.users_repository import UserRepository

from .connection_test import SessionLocalTest


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


def test_insert_user(data):
    users_repository = UserRepository(session=SessionLocalTest)
    user = users_repository.insert_user(
        first_name=data["name"],
        last_name=data["last_name"],
        age=data["age"],
    )

    assert isinstance(user, User)


def test_select_user(data):
    users_repository = UserRepository(session=SessionLocalTest)
    user = users_repository.select_user(first_name=data["name"])
    assert isinstance(user, List)
    assert user[0].id == 1
    assert user[0].first_name == data["name"]
    assert user[0].last_name == data["last_name"]
    assert user[0].age == data["age"]


def test_delete_user(data):
    users_repository = UserRepository(session=SessionLocalTest)
    users_repository.delete_user(user_id=1)
    user = users_repository.select_user(first_name=data["name"])
    assert user == []
