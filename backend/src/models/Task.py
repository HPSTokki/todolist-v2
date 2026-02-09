from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from sqlalchemy import Boolean, String, Float
from typing import Optional, List

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(sa_type=String, index=True, nullable=False)
    is_completed: str = Field(default="Pending", sa_type=String, nullable=False)

class InsertTask(BaseModel):
    title: str
    is_completed: str = "Pending"

class UpdateTask(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[str] = None

class ReadTask(BaseModel):
    id: int
    title: str
    is_completed: str

class TaskResponse(BaseModel):
    tasks: List[Task]