# Contain business logic
from sqlalchemy.orm import Session

from app.repositories.departments import Department_Repository
from pydantic import EmailStr, TypeAdapter
from app.exceptions.common_exception import InvalidEmailException, InvalidIdException, EmptyTableException
from app.exceptions.department_exceptions import InvalidDepartmentNameException

email_adapter = TypeAdapter(EmailStr)

class Depatrment_Service:
    name = "Department"
    @staticmethod
    def get_all_department(db: Session):
        department_list = Department_Repository.get_all_department(db)
        if not department_list:
            raise EmptyTableException(Depatrment_Service.name)
        else:
            return department_list


    @staticmethod
    def get_department_by_id(department_id, db):
        department_data = Department_Repository.get_department_by_id(department_id, db)
        if not department_data:
            raise InvalidIdException('Department', department_id)
        else:
            return department_data

    @staticmethod
    def get_department_by_name(department_name, db):
        valid_department_name = department_name.title()
        department_data = Department_Repository.get_department_by_name(valid_department_name, db)
        if not department_data:
            raise InvalidDepartmentNameException(department_name)
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
            raise InvalidEmailException()

        department = Department_Repository.update_department_email(department_id,
                                                                   valid_email,
                                                                   db)

        if not department:
            raise InvalidIdException("Department", department_id)
        else:
            return department


    @staticmethod
    def delete_department(department_id, db):
        department = Department_Repository.delete_department(department_id,db)
        if not department:
            raise InvalidIdException("Department", department_id)
        else:
            return {"status": f"{department.name} deleted successfull"}

