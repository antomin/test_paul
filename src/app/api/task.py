from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
async def tasks_list_view():
    pass


@router.get("/{task_id}")
async def tasks_detail_view():
    pass


@router.post("/{task_id}")
async def tasks_create_view():
    pass


@router.patch("/{task_id}")
async def tasks_update_view():
    pass
