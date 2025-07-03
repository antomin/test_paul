from datetime import datetime

from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column

from ..enums import TaskStatus
from .base import Base


class Task(Base["Task"]):
    __tablename__ = "tasks"

    title: Mapped[str]
    description: Mapped[str]
    due_date: Mapped[datetime]
    status: Mapped[TaskStatus] = mapped_column(ENUM(TaskStatus))
