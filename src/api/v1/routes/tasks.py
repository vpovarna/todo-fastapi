from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from db.repositories.tasks import TasksRepository, get_tasks_repository
from domain.response import Response
from domain.task import Task, TaskInDB
from schemas.tasks import TaskItemCreate

# TODO: Add security dependency
router = APIRouter()


@router.post("", response_model=Response[Task], status_code=HTTP_201_CREATED)
def create_task(create_task: TaskItemCreate, tasks_repo: TasksRepository = Depends(get_tasks_repository)) -> Response:
    """
    Create new task.
    """
    db_task = tasks_repo.create(create_task)
    return Response(data=Task(id=db_task.id), message="Task created successfully", status_code=HTTP_201_CREATED)


@router.get("/{task_id}", response_model=Response[TaskInDB], status_code=HTTP_200_OK)
def get_task(task_id: int, tasks_repo: TasksRepository = Depends(get_tasks_repository)) -> Response:
    """"
    Retrieves a task by `task_id`.
    """

    db_task = tasks_repo.get_task(task_id)

    if db_task is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Task not found")

    task_in_db = TaskInDB(
        id=db_task.id,
        title=db_task.title,
        description=db_task.description,
        completed=db_task.completed,
        completed_at=db_task.completed_at
    )
    print(task_in_db)
    return Response(data=task_in_db, status_code=HTTP_200_OK)

# @router.delete("/{task_id")
# def delete_task(task_id: int) -> Response:
#     """
#     Delete a task by id
#     """
#     return Response(message="Task deleted", status_code=HTTPStatus.NO_CONTENT)
#
#
# @router.put("/{task_id}", response_model=Response[TaskDTO], status_code=HTTPStatus.OK)
# def update_task(task_id: int, task: CreateTask) -> Response:
#     """
#     Update a task by id
#     """
#     return Response(message="Task updated", status_code=HTTPStatus.OK)
