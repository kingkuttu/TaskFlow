from fastapi import APIRouter
from app.schemas.task import Task, TaskCreate
from app.services import task_service

router = APIRouter()

@router.get("/")
def get_tasks() -> list[Task]:
    return task_service.get_tasks()

@router.get("/{task_id}")
def get_task(task_id: int) -> Task:
    return task_service.get_task(task_id)

@router.post("/")
def create_task(task: TaskCreate) -> Task:
    return task_service.create_task(task)

@router.put("/{task_id}")
def update_task(task_id: int, task: TaskCreate) -> Task:
    return task_service.update_task(task_id, task)

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:
    task_service.delete_task(task_id)