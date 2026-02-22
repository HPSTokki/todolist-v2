from sqlmodel import Session, select

from src.dto.todolist_dto import InsertUser, ListReadUser
from src.models.todolist_model import User, Task

class UserService():
    def __init__(self, session: Session):
        self.session = session
        
    def get_all_user(self) -> ListReadUser:
        stmt = select(User)
        result = self.session.exec(stmt).all()
        
        return {
            "users": result
        }
        