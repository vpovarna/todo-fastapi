from typing import Optional

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.session import get_db
from db.tasks import Task
from domain.task import TaskBase, TaskInUpdate


class TasksRepository:
    """
    Repository to manipulate with task.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, create_task: TaskBase) -> Task:
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
        """
        Get a task from the database
        """
        return self.db.query(Task).filter(Task.id == task_id).first()

    def delete_task(self, task_id: int) -> Task:
        """
        Delete a task from the database
        """
        db_todo = self.db.query(Task).filter(Task.id == task_id).first()
        self.db.delete(db_todo)
        self.db.commit()
        return db_todo

    def update_task(self, task: Task, create_task_item: TaskInUpdate) -> Task:
        """
        Update a task from the database
        """

        task_data = jsonable_encoder(task)
        update_task_data = create_task_item.dict(exclude_unset=True)
        for field in task_data:
            if field in update_task_data:
                setattr(task, field, update_task_data[field])

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task


def get_tasks_repository(db: Session = Depends(get_db)) -> TasksRepository:
    return TasksRepository(db)
