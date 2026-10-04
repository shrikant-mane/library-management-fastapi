from app.repositories.admin import AdminRepository
from app.models.admin import Admin
from app.exceptions.common_exception import InvalidEmailException,InvalidIdException, EmptyTableException
from app.exceptions.admin_exception import EmptyAdminTableException, AdminDoesNotExistException
from pydantic import EmailStr, TypeAdapter
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

email_adapter = TypeAdapter(EmailStr)

class AdminService:
    name = "Admin"

    @staticmethod
    def get_all_admin(db):
        admin_list = AdminRepository.get_all_admin(db)
        if not admin_list:
            raise EmptyTableException(AdminService.name)
        else:
            return admin_list


    @staticmethod
    def get_admin_by_id(admin_id, db):
        admin_data = AdminRepository.get_admin_by_id(admin_id, db)
        if not admin_data:
            raise InvalidIdException(AdminService.name, admin_id)
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
            raise InvalidEmailException()

        admin = AdminRepository.update_admin_email(admin_id, valid_email, db)
        if not admin:
            raise AdminDoesNotExistException()
        else:
            return admin


    @staticmethod
    def delete_admin(admin_id, db):
        admin = AdminRepository.delete_admin(admin_id,db)
        if not admin:
            raise AdminDoesNotExistException()
        else:
            return {"status": f"{admin.username} deleted successfull"}


