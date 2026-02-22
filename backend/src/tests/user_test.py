import pytest
from pprint import pprint
from sqlmodel import SQLModel, Session, create_engine

from src.dto.todolist_dto import InsertUser
from src.services.user_service import UserService


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
        
def test_get_all_user(session):
    
    service = UserService(session)
    
    demo_data = []
    user_data = InsertUser(
        email="testmail@gmail.com",
        password="testpass123"
    )
    user_data2 = InsertUser(
        email="testmail2@gmail.com",
        password="testpass123"
    )
    
    demo_data.append(user_data)
    demo_data.append(user_data2)
    
    for data in demo_data:
        service.register_user(data)
    
    result = service.get_all_user()
    pprint(result)
    
    for user in result["users"]:
        pprint(user)
        assert user.id is not None 