from fastapi import FastAPI
from app.routers import tasks
from app.core.database import Base, engine
from app.models import *

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks")
Base.metadata.create_all(bind=engine)