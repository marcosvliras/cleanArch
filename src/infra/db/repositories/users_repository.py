from src.infra.db.entities import User
from src.infra.db.settings.connection import SessionLocal


class UserRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> User:
        with SessionLocal() as session:
            try:
                new_user = User(
                    first_name=first_name, last_name=last_name, age=age
                )
                session.add(new_user)
                session.commit()
                return new_user
            except Exception as e:
                session.rollback()
                raise e
