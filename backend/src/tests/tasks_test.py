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
    pprint("Get All Task:" + str(result))
    pprint("-----------------------------------------------------------------")
    assert result is not None
    
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
    
    pprint("Get One Task:" + str(result))
    pprint("-----------------------------------------------------------------")
    assert result.title == "Do Dishes"

def test_delete_task_by_id(session):
    service = UserService(session)

    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    for data in task_data:
        service.add_task(data)
    result = service.delete_task_by_id(1)
    
    pprint("Delete One Task By ID" + str(result))
    pprint("-----------------------------------------------------------------")
    assert result.id == 1

def test_delete_task_by_name(session):
    service = UserService(session)

    task_data = [
        InsertTask(title="Do Dishes", description="Do Dishes NOW",due_date=datetime.now(timezone.utc),  is_completed=False),
        InsertTask(title="Do Dishes Again", description="Do Dishes LATER NOW", is_completed=False)
    ]
    for data in task_data:
        service.add_task(data)
    result = service.delete_task_by_name("Do Dishes")
    pprint("Delete One Task By Title" + str(result))
    pprint("-----------------------------------------------------------------")
    assert result.id == 1
    
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
    pprint("Update Task by ID" + str(result))
    pprint("-----------------------------------------------------------------")
    assert result.title == "Do Something"
    assert result.is_completed is True
    