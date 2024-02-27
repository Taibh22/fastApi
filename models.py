# models.py
from sqlalchemy import Column, Integer, String
from database import Base

# Define the Task class from Base
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(String(256))