from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db
from db.tasks import Task
from schemas.tasks import TaskItemCreate


class TasksRepository:
    """
    Repository to manipulate with task.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, create_task: TaskItemCreate) -> Task:
        """
        Create a new task in the database
        """
        db_task = Task(
            title=create_task.title,
            description=create_task.description
        )

        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()


def get_tasks_repository(db: Session = Depends(get_db)) -> TasksRepository:
    return TasksRepository(db)
