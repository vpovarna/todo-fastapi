from typing import Optional, TypeVar, Generic, Dict, Any

from pydantic import BaseModel

ResponseData = TypeVar("ResponseData")


class Response(BaseModel, Generic[ResponseData]):
    success: bool = True
    data: Optional[ResponseData] = None
    message: Optional[str] = None
    errors: Optional[list] = None

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Exclude `null` values from response"""
        kwargs.pop("exclude_none", None)
        return super().dict(*args, exclude_none=True, **kwargs)
