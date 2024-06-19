from pydantic import BaseModel, Field, root_validator


class TaskDTO(BaseModel):
    id: int
    title: str = Field(..., title="Task title")
    done: bool = Field(..., title="Task status")

    class Config:
        orm_mode = True
        fields_order = ['id', 'title', 'done']


class CreateTask(BaseModel):
    title: str = Field(..., title="Task title")
