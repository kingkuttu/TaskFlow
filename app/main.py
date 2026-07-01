from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hellos"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}

@app.get("/search")
def search_tasks(status: str = "all"):
    return {
        "status": status
    }