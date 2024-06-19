from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False
    created_at: datetime = datetime.now()
    completed_at: datetime = None


class TaskItemCreate(BaseModel):
    title: str
    description: str = None
