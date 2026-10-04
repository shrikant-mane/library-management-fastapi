from fastapi import APIRouter, Depends, status
from app.core.database import get_db
from sqlalchemy.orm import Session

from app.services.departments import Depatrment_Service
from app.schemas.departments import CreateDepartment, ResponseDepartment

from app.security.auth import get_current_admin

router = APIRouter(
    prefix='/department',
    tags=['department'],
    dependencies=[Depends(get_current_admin)]

)


# Route → Service → Repository → Database


@router.get('/get', response_model=list[ResponseDepartment])
async def get_all_department(db: Session = Depends(get_db)):
    return Depatrment_Service.get_all_department(db)


@router.get('/id',response_model=ResponseDepartment)
async def get_department(department_id : int, db: Session = Depends(get_db)):
    return Depatrment_Service.get_department_by_id(department_id, db)


@router.get('/name',response_model=ResponseDepartment)
async def get_department_by_name(department_name : str, db: Session = Depends(get_db)):
    return Depatrment_Service.get_department_by_name(department_name, db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_department(department_data : CreateDepartment, db: Session = Depends(get_db)):
    return Depatrment_Service.create_department(department_data, db)


@router.put('/update', response_model=ResponseDepartment)
async def update_department_email(department_id: int, department_email: str, db: Session = Depends(get_db)):
    return Depatrment_Service.update_department_email(department_id, department_email, db)


@router.delete('/delete/{department_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id: int, db: Session = Depends(get_db)):
    return Depatrment_Service.delete_department(department_id, db)
