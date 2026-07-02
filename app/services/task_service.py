from fastapi import HTTPException
from app.schemas.task import Task, TaskCreate

tasks: list[Task] = []

def get_tasks():
    return tasks

def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

def create_task(task: TaskCreate):
    new_id = len(tasks) + 1
    new_task = Task(id=new_id, title=task.title)
    tasks.append(new_task)

    return new_task

