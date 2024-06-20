from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str]
    completed: bool = False


class Task(TaskBase):
    id: int


class TaskInDB(Task):
    created_at: datetime = datetime.now()
    completed_at: datetime = None


class TaskInUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
