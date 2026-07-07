from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.repositories import task_repository
from app.schemas.task import TaskCreate

def get_tasks(db: Session) -> list[Task]:
    return task_repository.get_tasks(db)

def get_task(db: Session, task_id: int) -> Task:
    task = task_repository.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

def create_task(db: Session, task_create: TaskCreate) -> Task:
    task = Task(title=task_create.title)

    task_repository.create_task(db, task)
    db.commit()

    return task

def update_task(db: Session, task_id: int, task_update: TaskCreate) -> Task:
    task = get_task(db, task_id)

    task.title = task_update.title

    task_repository.update_task(db, task)
    db.commit()

    return task

def delete_task(db: Session, task_id: int) -> None:
    task = get_task(db, task_id)

    task_repository.delete_task(db, task)
    db.commit()