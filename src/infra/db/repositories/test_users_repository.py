from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.db.entities import User
from src.infra.db.settings.base import Base

from .users_repository import UserRepository

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(bind=engine)
# Base.metadata.create_all(bind=engine)


# def test_insert_user():
#    mocked_first_name = "Any First Name"
#    mocked_last_name = "Any Last Name"
#    mocked_age = 99
#
#    users_repository = UserRepository()
#    user = users_repository.insert_user(
#        first_name=mocked_first_name,
#        last_name=mocked_last_name,
#        age=mocked_age,
#    )
#
#    assert isinstance(user, User)
