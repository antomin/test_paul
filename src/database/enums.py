from enum import StrEnum


class TaskStatus(StrEnum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
