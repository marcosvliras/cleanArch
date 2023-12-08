from typing import Dict

from src.data.interfaces.users_repository import UserRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.user_delete import UserDeleteInterface


class UserDelete(UserDeleteInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def delete(self, user_id: int) -> Dict:
        return self.__user_repository.delete_user(user_id)
