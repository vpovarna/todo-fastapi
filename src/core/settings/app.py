import logging
from typing import List

from pydantic import BaseModel


class AppSettings(BaseModel):
    """
    Base application settings
    """

    api_prefix: str = "/api/v1"
    allowed_hosts: List[str] = ["*"]
    logging_level: int = logging.INFO

    # database_url: str
    min_connections_count: int = 5
    max_connections_count: int = 10

    class Config:
        env_file = ".env"
