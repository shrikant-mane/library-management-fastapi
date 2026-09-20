from fastapi import APIRouter, Depends
from app.core.config import settings
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import SessionLocal, get_db

router = APIRouter(
    prefix='/Routes',
    tags=['checks']
)

# APIRouter in FastAPI. It is mainly used to group related API endpoints together.
# tags is mainly used for Swagger/OpenAPI documentation

"""
in docs
checks
  GET  /Routes/database
"""

@router.get('/env')
async def get_env():
    try:
        # return {'DATABASE_URL': settings.DATABASE_URL}
        if settings.DATABASE_URL:
            return {'status': 'env access successful.'}
    except Exception as ex:
        raise ex

@router.get('/database')
async def database_connection_check(db: Session = Depends(get_db)):
    try:
        db.execute(text('select 1'))
        return {'status': 'database connection successful.'}

    except Exception as ex:
        return {
            'status': 'database connection failed',
            'error': str(ex)
        }

