from core.models.status import Status
from fastapi import APIRouter
from version import response

router = APIRouter()


@router.get("", response_model=Status)
def status():
    """
    Health check endpoint
    """
    return Status(**response)
