from datetime import datetime

from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from ..enums import TaskStatus


class Task(Base["Task"]):
    __tablename__ = "tasks"

    title: Mapped[str]
    description: Mapped[str]
    due_date: Mapped[datetime]
    status: Mapped[TaskStatus] = mapped_column(ENUM(TaskStatus))
