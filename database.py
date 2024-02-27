from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of SQLite engine
engine = create_engine("sqlite:///fastapidb.db")

# Create an instance of DeclarativeBase
Base = declarative_base()

# Create the SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Function to get a new session
def get_session():
    return SessionLocal()