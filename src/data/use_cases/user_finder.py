from typing import Dict

from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def create(self, first_name: str, last_name: str, age: int) -> Dict:
        return self.__user_repository.insert_user(first_name, last_name, age)

    def find(self, first_name) -> Dict:
        return self.__user_repository.select_user(first_name)

    def delete(self, user_id: int) -> None:
        return self.__user_repository.delete_user(user_id)
