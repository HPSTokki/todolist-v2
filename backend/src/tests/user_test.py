import pytest
from sqlmodel import SQLModel, Session, create_engine

from src.services.user_service import UserService


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
        
def test_get_all_user(session):
    service = UserService(session)
    result = service.get_all_user()
    
    assert result == { "users": [] }