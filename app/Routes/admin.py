from fastapi import APIRouter, Depends, status
from app.core.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.services.admin import AdminService
from app.schemas.admin import CreateAdmin, ResponseAdmin
from pydantic import EmailStr

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


@router.get('/get', response_model=list[ResponseAdmin])
async def get_all_admin(db: Session = Depends(get_db)):
    return AdminService.get_all_admin(db)


@router.get('/get/id', response_model=ResponseAdmin)
async def get_admin_by_id(admin_id: int, db: Session = Depends(get_db)):
    return AdminService.get_admin_by_id(admin_id, db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_admin(admin_data: CreateAdmin, db: Session = Depends(get_db)):
    return AdminService.create_admin(admin_data, db)


@router.put('/update', response_model=ResponseAdmin)
async def update_admin_email(admin_id: int, admin_email: str, db: Session = Depends(get_db)):
    return AdminService.update_admin_email(admin_id, admin_email, db)


@router.delete('/delete/{admin_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    return AdminService.delete_admin(admin_id, db)