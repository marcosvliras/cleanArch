from abc import ABC, abstractmethod
from typing import List, Union

from src.infra.db.entities import User as UserEntity


class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(
        self, first_name: str, last_name: str, age: int
    ) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def select_user(self, user_id: int) -> Union[List[UserEntity], None]:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError
