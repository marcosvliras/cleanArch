from sqlalchemy import Engine, create_engine


class DBConnectionHandler:
    """DBConnectionHandler Class."""

    def __init__(self) -> None:
        """Constructor."""
        self.__connection_string = "sqlite:///foo.db"
        self.__engine = self.__create_databas_engine()

    def __create_databas_engine(self) -> Engine:
        """Return the engine connection."""
        return create_engine(self.__connection_string)

    def get_engine(self) -> Engine:
        """Return the engine connection."""
        return self.__engine
