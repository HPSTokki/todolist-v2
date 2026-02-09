from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.engine import get_session, SessionDep
from src.services.task_service import *
from src.models.Task import *
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# GET Funcs

@router.get("/", response_model=TaskResponse)
def getTask(session: SessionDep):
    return get_task(session)

@router.get("/{task_id}", response_model=Task)
def getOneTask(task_id: int, session: SessionDep):
    return get_one_task(task_id, session)

# POST Funcs

@router.post("/")
def addTask(task_data: InsertTask, session: SessionDep):
    return add_task(task_data, session)


# DELETE Funcs

@router.delete("/{task_id}")
def deleteTask(task_id: int, session: SessionDep):
    return delete_task(task_id, session)

# PUT/PATCH Funcs

@router.put("/{task_id}", response_model=Task)
def updateTask(task_id: int, task_data: UpdateTask, session: SessionDep):
    return update_task(task_id, task_data, session)
