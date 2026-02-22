from pydantic import BaseModel
from datetime import datetime

class InsertUser(BaseModel):
    email: str
    password: str
    
class ReadUser(BaseModel):
    id: int
    created_at: datetime
    
class ListReadUser(BaseModel):
    users: list[ReadUser]