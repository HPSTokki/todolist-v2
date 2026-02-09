from sqlmodel import Session, select
from fastapi import HTTPException
from typing import List
from src.models.Task import *

def add_task(task_data: InsertTask, session: Session):
    task = Task.model_validate(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task(session: Session) -> List[Task]:
    stmt = select(Task)
    tasks = session.exec(stmt).all()
    return { "tasks": tasks }

def get_one_task(task_id: int, session: Session):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task

def delete_task(task_id: int, session: Session):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task either deleted or not founnd")
    session.delete(task)
    session.commit()
    return {
        "message": "Task Deleted!"
    }

def update_task(task_id: int, task_data: UpdateTask, session: Session):
    task = session.get(Task, task_id)
    
    # Rebinding the value here and doing for loop to set the right attribute
    # for - in basically sets all attribute partial edit or not to allow input
    updated_task = task_data.model_dump(exclude_unset=True)
    for key, value in updated_task.items():
        setattr(task, key, value)

    session.commit()
    session.refresh(task)
    
    return {
        "message": "Task Updated!"
    }
