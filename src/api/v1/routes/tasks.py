from typing import List

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from db.repositories.tasks import TasksRepository, get_tasks_repository
from domain.response import Response
from domain.task import TaskBase, Task, TaskInDB, TaskInUpdate

# TODO: Add security dependency
router = APIRouter()


# TODO: Validate models (DB / DAO)

@router.post("", response_model=Response[Task], status_code=HTTP_201_CREATED)
def create_task(task_base: TaskBase, tasks_repo: TasksRepository = Depends(get_tasks_repository)) -> Response:
    """
    Create new task.
    """
    db_task = tasks_repo.create(task_base)
    return Response(data=db_task, message="Task created successfully", status_code=HTTP_201_CREATED)


@router.get("/{task_id}", response_model=Response[TaskBase], status_code=HTTP_200_OK)
def get_task(task_id: int, tasks_repo: TasksRepository = Depends(get_tasks_repository)) -> Response:
    """"
    Retrieves a task by `task_id`.
    """

    db_task = tasks_repo.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Task not found")

    task_in_db = TaskBase(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        completed_at=db_task.completed_at
    )
    print(task_in_db)
    return Response(data=task_in_db, status_code=HTTP_200_OK)


@router.delete("/{task_id}", status_code=HTTP_204_NO_CONTENT)
def delete_task(task_id: int, task_repo: TasksRepository = Depends(get_tasks_repository)):
    """
    Delete a task by id
    """
    db_task = task_repo.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Task not found")

    task_repo.delete_task(task_id)
    return Response(message=f"Task with id: {task_id} has been deleted.", status_code=HTTP_204_NO_CONTENT)


@router.put("/{task_id}", status_code=HTTP_200_OK)
def update_task(task_id: int, task: TaskInUpdate,
                task_repo: TasksRepository = Depends(get_tasks_repository)) -> Response:
    """
    Update a task by id
    """
    db_task = task_repo.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Task not found")

    task_repo.update_task(db_task, task)
    return Response(message="Task updated", status_code=HTTP_200_OK)


@router.get("", response_model=Response[List[TaskBase]], status_code=HTTP_200_OK)
def get_todos(skip: int = 0, limit: int = 100, task_repo: TasksRepository = Depends(get_tasks_repository)):
    """
    Return all tasks
    """
    todos = task_repo.get_all(skip=skip, limit=limit)
    return Response(data=todos, status_code=HTTP_200_OK)
