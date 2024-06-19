from typing import Optional, TypeVar, Generic, Dict, Any

from pydantic.generics import GenericModel

ResponseData = TypeVar("ResponseData")


class Response(GenericModel, Generic[ResponseData]):
    success: bool = True
    data: Optional[ResponseData] = None
    message: Optional[str] = None
    errors: Optional[list] = None

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Exclude `null` values from response"""
        kwargs.pop("exclude_none", None)
        return super().dict(*args, exclude_none=True, **kwargs)
