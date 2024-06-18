import logging
from typing import List

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Base application settings
    """

    api_prefix: str = "/api/v1"
    allowed_hosts: List[str] = ["*"]
    logging_level: int = logging.INFO

    database_url: str
    min_connection_count: int = 5
    max_connection_count: int = 10

    class Config:
        validate_assignment = True
