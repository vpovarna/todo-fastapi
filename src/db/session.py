from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import get_app_config

# TODO: Add settings

app_config = get_app_config()

session = create_engine(url=app_config.database.url, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=session)


def get_db() -> Generator:
    """
    Generate dependency yield database connection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
