from fastapi import APIRouter

from api.v1.routes import status, tasks

router = APIRouter()

router.include_router(router=status.router, tags=["Status"], prefix="/status")
router.include_router(router=tasks.router, tags=["Tasks"], prefix="/tasks")
