from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.admin import AdminRepository
from app.models.admin import Admin
from app.exceptions.admin_exception import InvalidADminEmailException
from pydantic import EmailStr, TypeAdapter, ValidationError
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

email_adapter = TypeAdapter(EmailStr)


class AdminService:

    @staticmethod
    def get_all_admin(db):
        admin_list = AdminRepository.get_all_admin(db)
        if not admin_list:
            raise HTTPException(
                status_code=404,
                detail="Admin table is empty"
            )
        else:
            return admin_list


    @staticmethod
    def get_admin_by_id(admin_id, db):
        admin_data = AdminRepository.get_admin_by_id(admin_id, db)
        if not admin_data:
            raise HTTPException(
                status_code=404,
                detail="Invalid department id"
            )
        else:
            return admin_data


    @staticmethod
    def create_admin(admin_data, db):
        admin_password = password_hash.hash(admin_data.password)
        admin_valid_data = Admin(
            id=admin_data.id,
            username=admin_data.username,
            first_name = admin_data.first_name,
            last_name = admin_data.last_name,
            email = admin_data.email,
            password = admin_password
        )
        return AdminRepository.create_admin(admin_valid_data, db)


    @staticmethod
    def update_admin_email(admin_id, admin_email, db):
        try:
            valid_email = email_adapter.validate_python(admin_email)
        except :
            raise InvalidADminEmailException("Please provide valid email address")

        admin = AdminRepository.update_admin_email(admin_id, valid_email, db)
        if not admin:
            raise HTTPException(
                status_code=404,
                detail="Invalid admin id"
            )
        else:
            return admin


    @staticmethod
    def delete_admin(admin_id, db):
        admin = AdminRepository.delete_admin(admin_id,db)
        if not admin:
            raise HTTPException(
                status_code=404,
                detail="Admin does not exist"
            )
        else:
            return {"status": f"{admin.username} deleted successfull"}


