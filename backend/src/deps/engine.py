from typing import Annotated, Generator
from sqlmodel import Session, create_engine
from fastapi import Depends
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent.parent
LOCAL_DB_PATH = BASE_PATH / "local.db"

sqlite_url = f"sqlite:///{LOCAL_DB_PATH}"
connect_args = { "check_same_thread": False }

engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

# Made into Reusable Annotated DB Dependency
SessionDep = Annotated[Session, Depends(get_session)]