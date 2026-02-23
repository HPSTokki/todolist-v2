from sqlmodel import Session, select

from src.dtos.todolist_dto import InsertTask
from src.models.todolist_model import Task


class UserService:
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

        return result

    def get_one_task_by_id(self, task_id: int) -> Task:
        stmt = select(Task, task_id)
        result = self.session.exec(stmt).first()
        return result

    def get_one_task_by_title(self, task_name: str) -> Task:
        stmt = select(Task).where(Task.title.ilike(f"{task_name}"))

        result = self.session.exec(stmt).first()

        return result
