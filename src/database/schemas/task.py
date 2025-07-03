from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ..enums import TaskStatus


class TaskBaseSchema(BaseModel):
    title: str
    description: str
    due_date: datetime
    status: TaskStatus


class TaskSchema(TaskBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    modified_at: datetime


class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(TaskBaseSchema):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None
    status: TaskStatus | None = None
