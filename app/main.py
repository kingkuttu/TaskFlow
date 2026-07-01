from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hellos"}

app.include_router(tasks.router)