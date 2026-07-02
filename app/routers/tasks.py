from fastapi import APIRouter, HTTPException
from app.schemas.task import Task, TaskCreate
from app.services import task_service

router = APIRouter()

@router.get("/")
def get_tasks():
    return task_service.get_tasks()

@router.get("/{task_id}")
def get_task(task_id: int):
    return task_service.get_task(task_id)

@router.post("/")
def create_task(task: TaskCreate):
    return task_service.create_task(task)
