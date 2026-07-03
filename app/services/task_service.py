from fastapi import HTTPException
from app.schemas.task import Task, TaskCreate

tasks: list[Task] = []

def get_tasks() -> list[Task]:
    return tasks

def get_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

def create_task(task: TaskCreate) -> Task:
    new_id = len(tasks) + 1
    new_task = Task(id=new_id, title=task.title)
    tasks.append(new_task)

    return new_task

def update_task(task_id: int, task: TaskCreate) -> Task:
    found_task = get_task(task_id)
    found_task.title = task.title
    
    return found_task

def delete_task(task_id: int) -> None:
    found_task = get_task(task_id)
    tasks.remove(found_task)
