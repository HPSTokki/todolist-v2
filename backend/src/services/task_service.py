from sqlmodel import Session, select

from src.dtos.todolist_dto import InsertTask, ListReadTask, ReadTask, UpdateTask
from src.models.todolist_model import Task

from src.exception import TaskNotFound

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def add_task(self, task_data: InsertTask) -> Task: # FINISHED
        task = Task(**task_data.model_dump(exclude_unset=True))
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_all_task(self) -> ListReadTask: # FINISHED
        stmt = select(Task)
        result = self.session.exec(stmt).all()
        tasks_lists = [ReadTask.model_validate(task) for task in result]
        return ListReadTask(tasks=tasks_lists)
    
    def get_all_task_raw(self) -> list[Task]: # FINISHED
        stmt = select(Task)
        result = self.session.exec(stmt).all()
        return result

    def get_one_task_by_id(self, task_id: int) -> Task | None: # FINISHED
        stmt = select(Task).where(Task.id == task_id)
        result = self.session.exec(stmt).first()
        if not result:
            raise TaskNotFound("Task Not Found")
        return result

    def get_one_task_by_title(self, task_name: str) -> Task | None: # FINISHED
        stmt = select(Task).where(Task.title.ilike(f"%{task_name}%"))
        result = self.session.exec(stmt).first()
        if not result:
            raise TaskNotFound(f"Task not found with title: {task_name}")
        return result
    
    def delete_task_by_id(self, task_id: int) -> Task | None:
        stmt = select(Task).where(Task.id == task_id) 
        result = self.session.exec(stmt).first()
        if not result: 
            raise TaskNotFound("Task doesn't exists")
        self.session.delete(result)
        self.session.commit()
        return result

    def delete_task_by_name(self, task_name: str) -> Task | None:
        task = self.session.exec(select(Task).where(Task.title.ilike(f"%{task_name}%"))).first()
        if not task:
            raise TaskNotFound("Task doesn't exists")
        self.session.delete(task)
        self.session.commit()
        return task
    
    def update_task_by_id(self, task_id: int, update_data: UpdateTask) -> Task | None:
        task = self.session.get(Task, task_id)
        if not task:
            raise TaskNotFound("Task doesn't exists")
        updated_data = update_data.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return task