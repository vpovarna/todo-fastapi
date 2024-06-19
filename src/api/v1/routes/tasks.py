from http import HTTPStatus

from fastapi import APIRouter

from domain.response import Response
from domain.tasks import TaskDTO, CreateTask

# TODO: Add security dependency
router = APIRouter()


@router.get("/{task_id}", response_model=Response[TaskDTO], status_code=HTTPStatus.OK)
def get_task(task_id: int) -> Response:
    """"
    Retrieves a task by `task_id`.
    """

    task_dto = TaskDTO(
        id=task_id,
        title="Test task",
        done=False
    )
    return Response(data=task_dto, status_code=HTTPStatus.OK)


@router.post("", response_model=Response[TaskDTO], status_code=HTTPStatus.CREATED)
def create_task(task: CreateTask) -> Response:
    """
    Create a new task
    """

    task_dto = TaskDTO(
        title=task.title,
        id=1,
        done=False
    )

    return Response(data=task_dto.dict(), message="The task was successfully created", status_code=HTTPStatus.CREATED)


@router.delete("/{task_id")
def delete_task(task_id: int) -> Response:
    """
    Delete a task by id
    """
    return Response(message="Task deleted", status_code=HTTPStatus.NO_CONTENT)


@router.put("/{task_id}", response_model=Response[TaskDTO], status_code=HTTPStatus.OK)
def update_task(task_id: int, task: CreateTask) -> Response:
    return Response(message="Task updated", status_code=HTTPStatus.OK)
