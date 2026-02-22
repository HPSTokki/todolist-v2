from pydantic import BaseModel, Field
from datetime import datetime

from src.models.todolist_model import Task

class InsertTask(BaseModel):
    title: str = Field(min_length=3, max_length=128)
    description: str | None = Field(default=None, min_length=3, max_length=1000)
    due_date: datetime | None = None
    is_completed: bool = False
