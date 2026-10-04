from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import  get_db
from app.services.user import UserService
from app.schemas.user import UserCreate


router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.post('/create')
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(user_data, db)