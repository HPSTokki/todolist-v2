from datetime import datetime, timezone
from pprint import pprint 

import pytest
from sqlmodel import SQLModel, Session, create_engine, select

from src.dtos.todolist_dto import InsertTask
from src.models.todolist_model import Task

from src.services.task_service import UserService

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
        
def test_add_task(session):
    service = UserService(session)
    
    task_data = InsertTask(
        title="Eat Food",
        description="Eat Dinner Food",
        is_completed = True
    )
    
    result = service.add_task(task_data)
    
    assert result is not None
    assert result.title == "Eat Food"
    assert result.description == "Eat Dinner Food"
    assert result.is_completed is True
    
def test_add_and_get_tasks(session):
    service = UserService(session)
    
    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    
    for data in task_data:
        service.add_task(data)
    
    result = session.exec(select(Task)).all()
    pprint(result)
    assert result is not None
    