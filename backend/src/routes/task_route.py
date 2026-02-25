from fastapi import APIRouter, HTTPException, status

from src.models.todolist_model import Task
from src.dtos.todolist_dto import InsertTask, ListReadTask, ReadTask, UpdateTask
from src.deps.engine import SessionDep
from src.exception import TaskNotFound
from src.services.task_service import UserService

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/all", response_model=ListReadTask)
def get_all_tasks(session: SessionDep):
    service = UserService(session)
    tasks = service.get_all_task()
    return tasks

@router.get("/all-raw", response_model=list[Task])
def get_all_tasks(session: SessionDep):
    service = UserService(session)
    tasks = service.get_all_task_raw()
    return tasks

@router.post("/add", response_model=ReadTask)
def add_task(session: SessionDep, task_data: InsertTask):
    service = UserService(session)
    task = service.add_task(task_data)
    return task

@router.get("/task-title", response_model=ReadTask)
def get_one_task_by_title(session: SessionDep, task_title: str):
    service = UserService(session)
    try:
        task = service.get_one_task_by_title(task_title)
        return task
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

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
        
@router.delete("/delete/{task_id}", response_model=Task)
def delete_task_by_id(session: SessionDep, task_id: int):
    service = UserService(session)
    try:
        task = service.delete_task_by_id(task_id)
        return task
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found, nothing deleted"
        )