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

    class Config:
        validate_assignment = True
