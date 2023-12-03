import os

import pytest
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.db.entities import User
from src.infra.db.repositories.users_repository import UserRepository
from src.infra.db.settings.base import Base

current_directory = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{current_directory}/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocalTest = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


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


def test_select_user_by_id(data):
    users_repository = UserRepository(session=SessionLocalTest)
    user = users_repository.select_user_by_id(user_id=1)
    assert isinstance(user, User)
    assert user.id == 1
    assert user.first_name == data["name"]
    assert user.last_name == data["last_name"]
    assert user.age == data["age"]


def test_delete_user():
    users_repository = UserRepository(session=SessionLocalTest)
    users_repository.delete_user(user_id=1)
    user = users_repository.select_user_by_id(user_id=1)
    assert user is None
