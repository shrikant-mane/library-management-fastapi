from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# In SQLAlchemy, sessionmaker is a factory that creates database Session objects.
# A SQLAlchemy Session is basically the working interface between your Python application and the database.

"""
FastAPI Endpoint
       ↓
SessionLocal()
       ↓
SQLAlchemy Session
       ↓
SQLAlchemy Engine
       ↓
PostgreSQL

engine → manages communication with the database
sessionmaker → creates sessions configured to use that engine
Session → performs database operations
"""

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()

# declarative_base() tells SQLAlchemy: "The classes that inherit from this base represent database tables."

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


