from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}


@router.get("/search")
def search_tasks(status: str = "all"):
    return {
        "status": status
    }
