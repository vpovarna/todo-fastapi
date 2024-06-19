from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: int


class TaskInDB(Task):
    title: str
    description: str
    completed: bool
    completed_at: Optional[datetime]  # TODO; Teste completed_at
