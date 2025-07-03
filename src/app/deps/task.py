from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from database.interface import db
from database.models import Task


async def get_task_by_id(
    session: Annotated[AsyncSession, Depends(db.get_session)],
    task_id: Annotated[int, Path(..., description="Task ID")],
) -> Task:
    if task := await Task.get_by_id(task_id, session=session):
        return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
