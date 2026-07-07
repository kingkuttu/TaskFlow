from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.task import TaskCreate, TaskResponse
from app.services import task_service

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
) -> list[TaskResponse]:
    return task_service.get_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
) -> TaskResponse:
    return task_service.get_task(db, task_id)


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
) -> TaskResponse:
    return task_service.create_task(db, task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
) -> TaskResponse:
    return task_service.update_task(db, task_id, task)


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
) -> None:
    task_service.delete_task(db, task_id)