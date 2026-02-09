from sqlmodel import SQLModel, create_engine, Session
from typing import Generator, Annotated
from pathlib import Path
from fastapi import Depends
import os
from dotenv import load_dotenv

load_dotenv()

# This sets the base path to path /backend
BASE_PATH = Path(__file__).resolve().parent.parent

# Local DB path sets it to /backend/local.db
LOCAL_DB_PATH = BASE_PATH / "local.db"

# SUPABASE_DB is fetched by the getenv method in the .env file found in the /backend/env
SUPABASE_DB = os.getenv("SUPABASE_URL")

sqlite_url = f"sqlite:///{LOCAL_DB_PATH}"
connect_args = {
    "check_same_thread": False
}

# Two engine variations here, one is with SUPABASE_DB and other is for SQLite
# IF you want to test out locally, comment the top engine, uncomment the engine bellow also swap the env.py value if ever youd make changes to src/model files

engine = create_engine(SUPABASE_DB, echo=True)
# engine = create_engine(sqlite_url, connect_args=connect_args)


# Commented Code is for rapid db making, else use: alembic revision -m "message here" --autogenerate

# def create_db_and_model():
#     SQLModel.metadata.create_all(engine)

def get_session() -> Generator[SQLModel, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]