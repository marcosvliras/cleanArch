# pylint: disable=W0611

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.db.entities import User
from src.infra.db.settings.base import Base

current_directory = os.path.dirname(os.path.abspath(__file__))

# UNIT TESTS
SQLALCHEMY_DATABASE_URL = f"sqlite:///{current_directory}/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocalTest = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

# INTEGRATION TESTS
SQLALCHEMY_DATABASE_URL_INTEGRATION = (
    f"sqlite:///{current_directory}/test_integration.db"
)

engine_integration = create_engine(
    SQLALCHEMY_DATABASE_URL_INTEGRATION,
    connect_args={"check_same_thread": False},
)
SessionLocalTestIntegration = sessionmaker(bind=engine_integration)
Base.metadata.create_all(bind=engine_integration)
