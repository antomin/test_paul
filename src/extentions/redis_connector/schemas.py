from pydantic import BaseModel

from database.schemas.task import TaskSchema
from extentions.redis_connector.enums import TaskEvent


class TaskMessage(BaseModel):
    event: TaskEvent
    task: TaskSchema
