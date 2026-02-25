from datetime import datetime, timezone
from pprint import pprint 

import pytest
from sqlmodel import SQLModel, Session, create_engine, select

from src.dtos.todolist_dto import InsertTask, UpdateTask
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
    assert result.id == 1
    assert result.title == "Eat Food"
    assert result.description == "Eat Dinner Food"
    assert result.is_completed is True
    
def test_get_all_task(session):
    service = UserService(session)
    
    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    
    for data in task_data:
        service.add_task(data)
    result = service.get_all_task()
    assert len(result) == 2
    expected_title = ["Do Dishes", "Do Dishes Again"]
    expected_id = [1, 2]
    expected_description = ["Do Dishes NOW", "Do Dishes LATER NOW"]
    for id, task in enumerate(result):
        assert task.id == expected_id[id]
        assert task.title == expected_title[id]
        assert task.description == expected_description[id]
     
def test_get_one_task_by_title(session):
    service = UserService(session)
    
    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    
    for data in task_data:
        service.add_task(data)
    
    get_one_title = "Do Dishes" 
    
    result = service.get_one_task_by_title(get_one_title)
    
    assert result.title == "Do Dishes"

def test_get_one_task_by_id(session):
    service = UserService(session)
    
    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    
    for data in task_data:
        service.add_task(data)
    
    get_one_title = 1 
    
    result = service.get_one_task_by_id(get_one_title)
    
    assert result.id == 1 

def test_delete_task_by_id(session):
    service = UserService(session)

    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    for data in task_data:
        service.add_task(data)
    result = service.delete_task_by_id(1)
    assert result is not None
    deleted_task = service.get_all_task()
    assert all(task.id != 1 for task in deleted_task)

def test_delete_task_by_name(session):
    service = UserService(session)

    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    for data in task_data:
        service.add_task(data)
    result = service.delete_task_by_name("Do Dishes")
    assert result is not None
    deleted_task = service.get_all_task()
    assert all(task.title != "Do Dishes" for task in deleted_task)
    
def test_update_task_by_id(session):
    service = UserService(session)

    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    for data in task_data:
        service.add_task(data)
    update_data = UpdateTask(
        title="Do Something",
        is_completed=True
    ) 
    result = service.update_task_by_id(1, update_data)
    assert result.title == "Do Something"
    assert result.is_completed is True