import pytest

from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensitive test.")
def test_create_database_engine():
    """Test create database engine."""
    db_conn_handler = DBConnectionHandler()
    engine = db_conn_handler.get_engine()
    assert engine is not None
    assert str(engine.url) == "sqlite:///foo.db"
