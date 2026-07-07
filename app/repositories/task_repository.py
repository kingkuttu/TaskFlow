from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task

def create_task(db: Session, task: Task) -> None:
    db.add(task)
    db.flush()
    db.refresh(task)

def get_tasks(db: Session) -> list[Task]:
    statement = select(Task)

    return list(db.scalars(statement))

def get_task(db: Session, task_id: int) -> Task | None:
    statement = select(Task).where(Task.id == task_id)

    return db.scalar(statement)

def update_task(db: Session, task: Task) -> None:
    db.flush()
    db.refresh(task)

def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.flush()