from app.core.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
