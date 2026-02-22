from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import String
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(default=None, sa_type=String, unique=True, index=True)
    password: str = Field(default=None, sa_type=String, min_length=8, max_length=32)
    created_at: datetime = Field(default_factory=datetime.now)
    
    tasks: list["Task"] = Relationship(back_populates="user")
    
class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    title: str = Field(default=None, sa_type=String, index=True)
    description: str | None = Field(default=None, sa_type=String)
    is_completed: bool = Field(default=False)
    due_date: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    
    user: User | None = Relationship(back_populates="tasks")