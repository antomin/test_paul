from typing import Annotated

from fastapi import APIRouter, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps.task import get_task_by_id
from database.interface import db
from database.models import Task
from database.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskSchema])
async def tasks_list_view(session: Annotated[AsyncSession, Depends(db.get_session)]):
    tasks = await Task.get_all(session)

    return tasks


@router.get("/{task_id}", response_model=TaskSchema)
async def tasks_detail_view(task: Annotated[Task, Depends(get_task_by_id)]):
    return task


@router.post("/{task_id}", response_model=TaskSchema)
async def tasks_create_view(
    data: Annotated[TaskCreateSchema, Body(...)],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    task = await Task(**data.model_dump()).create(session)

    return task


@router.patch("/{task_id}", response_model=TaskSchema)
async def tasks_update_view(
    data: Annotated[TaskUpdateSchema, Body(...)],
    task: Annotated[Task, Depends(get_task_by_id)],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    task = await task.update(**data.model_dump(exclude_unset=True), session=session)

    return task


@router.delete("/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def tasks_delete_view(
    task: Annotated[Task, Depends(get_task_by_id)],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    await task.delete(session=session)
