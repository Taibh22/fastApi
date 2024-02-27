# schemas.py
from pydantic import BaseModel
from typing import Optional
import datetime

# Create Task schema (Pydantic Model)
class TaskCreate(BaseModel):
    title: str
    description: str

# Full Task schema (Pydantic Model)
class Task(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True

class CreateUser(BaseModel):
    name: str
    password: str

class UserLogin(BaseModel):
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class DataToken(BaseModel):
    id: Optional[str] = None

class UserOutput(BaseModel):
    name: str
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True