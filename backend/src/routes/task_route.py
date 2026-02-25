from fastapi import APIRouter, HTTPException, status

from src.models.todolist_model import Task
from src.dtos.todolist_dto import InsertTask, ListReadTask, ReadTask, UpdateTask
from src.deps.engine import SessionDep
from src.exception import TaskNotFound
from src.services.task_service import UserService

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/", response_model=ListReadTask | ReadTask)
def get_all_tasks(session: SessionDep, task_title: str | None = None):
    service = UserService(session)
    if task_title is not None:
        try:
            task = service.get_one_task_by_title(task_title)
            return task
        except TaskNotFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
    else:
        tasks = service.get_all_task()
    return tasks

@router.get("/raw", response_model=list[Task])
def get_all_tasks_raw(session: SessionDep):
    service = UserService(session)
    tasks = service.get_all_task_raw()
    return tasks

@router.post("/", response_model=ReadTask)
def add_task(session: SessionDep, task_data: InsertTask):
    service = UserService(session)
    task = service.add_task(task_data)
    return task

@router.delete("/{task_id}", response_model=Task)
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

@router.put("/{task_id}", response_model=ReadTask)
def update_task_by_id(session: SessionDep, task_id: int, update_data: UpdateTask):
    service = UserService(session)
    try:
        task = service.update_task_by_id(task_id, update_data)
        return task
    except TaskNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found, nothing deleted"
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