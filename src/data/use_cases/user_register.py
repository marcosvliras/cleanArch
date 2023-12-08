from typing import Dict, List

from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.user_register import UserRegisterInterface


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def create(self, first_name: str, last_name: str, age: int) -> None:
        self.__validate_name(first_name)
        self.__user_repository.insert_user(first_name, last_name, age)
        return None

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")

        if len(first_name) > 18:
            raise ValueError("First name must be less than 18 characters")
