from typing import List, Union

from sqlalchemy.orm.session import Session

from src.data.interfaces.users_repository import UserRepositoryInterface
from src.infra.db.entities import User as UserEntity


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def insert_user(
        self, first_name: str, last_name: str, age: int
    ) -> UserEntity:
        with self.__session() as session:
            try:
                new_user = UserEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                session.add(new_user)
                session.commit()
                return new_user
            except Exception as e:
                self.__session.rollback()
                raise e

    def select_user(self, first_name: str) -> Union[List[UserEntity], None]:
        with self.__session() as session:
            try:
                users = (
                    session.query(UserEntity)
                    .filter(UserEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as e:
                self.__session.rollback()
                raise e

    def delete_user(self, user_id: int) -> None:
        with self.__session() as session:
            try:
                session.query(UserEntity).filter(
                    UserEntity.id == user_id
                ).delete()
                session.commit()
            except Exception as e:
                self.__session.rollback()
                raise e
