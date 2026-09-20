from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.tests.setup.test_config import settings

test_engine = create_engine(
    settings.TEST_DATABASE_URL,
    pool_pre_ping=True
)

Test_SessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()

def override_get_db():
    db = Test_SessionLocal()

    try:
        yield db
    finally:
        db.close()



