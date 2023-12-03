from typing import Union

from sqlalchemy.orm.session import Session

from src.infra.db.entities import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def insert_user(self, first_name: str, last_name: str, age: int) -> User:
        with self.__session() as session:
            try:
                new_user = User(
                    first_name=first_name, last_name=last_name, age=age
                )
                session.add(new_user)
                session.commit()
                return new_user
            except Exception as e:
                self.__session.rollback()
                raise e

    def select_user_by_id(self, user_id: int) -> Union[User, None]:
        with self.__session() as session:
            try:
                return session.query(User).filter(User.id == user_id).first()
            except Exception as e:
                self.__session.rollback()
                raise e

    def delete_user(self, user_id: int) -> None:
        with self.__session() as session:
            try:
                session.query(User).filter(User.id == user_id).delete()
                session.commit()
            except Exception as e:
                self.__session.rollback()
                raise e
