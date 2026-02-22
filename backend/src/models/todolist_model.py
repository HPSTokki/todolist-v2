from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime, timezone

class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = Field(default=None, sa_type=String, index=True)
    description: str | None = Field(default=None, sa_type=String)
    due_date: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_completed: bool = Field(default_factory=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    