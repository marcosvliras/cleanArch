from typing import Dict, List

from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def create(self, first_name: str, last_name: str, age: int) -> Dict:
        return self.__user_repository.insert_user(first_name, last_name, age)

    def find(self, first_name) -> Dict:
        self.__validate_name(first_name)

        users = self.__search_user(first_name)
        response = self.__format_response(users)
        return response

    def delete(self, user_id: int) -> None:
        return self.__user_repository.delete_user(user_id)

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")

        if len(first_name) > 18:
            raise ValueError("First name must be less than 18 characters")

    def __search_user(self, first_name: str) -> List[Users]:
        users = self.__user_repository.select_user(first_name)
        if users == []:
            raise ValueError("User not found")
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        response = {"type": "Users", "count": len(users), "attributes": users}
        return response
