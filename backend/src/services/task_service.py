from sqlmodel import Session, select

from src.models.todolist_model import Task
from src.dtos.todolist_dto import InsertTask

class UserService():
    def __init__(self, session: Session):
        self.session = session
        
    def add_task(self, task_data: InsertTask) -> Task:
        task = Task(**task_data.model_dump(exclude_unset=True))
        
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task
    
    def get_all_task(self) -> list[Task]:
        stmt = select(Task)
        result = self.session.exec(stmt).all()
        
        return {
            "tasks": result
        }
        
        