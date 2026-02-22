from sqlmodel import Session, select

from src.core.security import hash_password
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
        
    def register_user(self, user_data: InsertUser) -> User:
        user = User.model_validate(user_data)
        
        hashed_password = hash_password(user_data.password)
        
        user.password = hashed_password
        
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        return user
        