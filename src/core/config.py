from core.settings.app import AppSettings
from functools import lru_cache


@lru_cache
def get_app_settings() -> AppSettings:
    """
    Return application config
    """
    return AppSettings()
