from fastapi import APIRouter, HTTPException, status

from src.models.todolist_model import Task
from src.dtos.todolist_dto import InsertTask, ReadTask, UpdateTask
from src.deps.engine import SessionDep
from src.exception import TaskNotFound
from src.services.task_service import UserService

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/", response_model=list[Task])
def get_all_tasks(session: SessionDep):
    service = UserService(session)
    tasks = service.get_all_task()
    return tasks

@router.get("/{task_id}", response_model=ReadTask)
def get_one_task_by_id(session: SessionDep, task_id: int):
    service = UserService(session)
    try:
        task = service.get_one_task_by_id(task_id)
        return task
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )