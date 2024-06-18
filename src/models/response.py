from typing import Generic, TypeVar, Optional, Dict, Any

from pydantic.generics import GenericModel

ResponseData = TypeVar("ResponseData")


class Response(GenericModel, Generic[ResponseData]):
    success: bool = True
    data: Optional[ResponseData] = None
    message: Optional[str] = None
    error: Optional[str] = None

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Exclude `null` values from the response."""
        kwargs.pop("exclude_none", None)
        return super().dict(*args, exclude_none=True, **kwargs)
