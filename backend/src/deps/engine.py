from pathlib import Path

from sqlmodel import Session, create_engine
from fastapi import Depends
from typing import Annotated, Generator

BASE_PATH = Path(__file__).resolve().parent.parent.parent
LOCAL_DB_PATH = BASE_PATH / "local.db"

SQLITE_URL = f"sqlite:///{LOCAL_DB_PATH}"
CONNECT_ARGS = { "check_same_thread": False }

engine = create_engine(SQLITE_URL, connect_args=CONNECT_ARGS, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
        
SessionDep = Annotated[Session, Depends(get_session)]