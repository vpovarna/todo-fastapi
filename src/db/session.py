from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker, declarative_base

from config.config import get_app_config

database_config = get_app_config().database

session = create_engine(
    url=database_config.db_url,
    echo=False,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=session)

Base = declarative_base()



def get_db() -> Generator:
    """
    Generate dependency yield database connection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
