# Contain business logic
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.departments import Department_Repository
from pydantic import EmailStr, TypeAdapter, ValidationError
from app.exceptions.department_exceptions import InvalidEmailException

email_adapter = TypeAdapter(EmailStr)

class Depatrment_Service:

    @staticmethod
    def get_all_department(db: Session):
        department_list = Department_Repository.get_all_department(db)
        if not department_list:
            return {'message': 'Department table is empty'}
        else:
            return department_list


    @staticmethod
    def get_department(department_id, db):
        department_data = Department_Repository.get_department(department_id, db)
        if not department_data:
            raise HTTPException(
                status_code=404,
                detail="Invalid department id"
            )
        else:
            return department_data


    @staticmethod
    def create_department(department_data, db):
       return Department_Repository.create_department(department_data, db)


    @staticmethod
    def update_department_email(department_id: int, department_email:str, db):
        try:
            valid_email = email_adapter.validate_python(department_email)
        except :
            raise InvalidEmailException("Please provide valid email address")

        department = Department_Repository.update_department_email(department_id, valid_email, db)
        if not department:
            raise HTTPException(
                status_code=404,
                detail="Invalid department id"
            )
        else:
            return department




    @staticmethod
    def delete_department(department_id, db):
        department = Department_Repository.delete_department(department_id,db)
        if not department:
            raise HTTPException(
                status_code=404,
                detail="Department does not exist"
            )
        else:
            return {"status": f"{department.name} deleted successfull"}