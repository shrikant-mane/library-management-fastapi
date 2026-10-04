from app.models.user import User
from app.repositories.departments import Department_Repository
from app.schemas.user import UserCreate
from pydantic import EmailStr, TypeAdapter, ValidationError
from app.repositories.user import UserRepository
from app.exceptions.common_exception import InvalidEmailException, EmailAlreadyRegisteredException
from app.exceptions.department_exceptions import InvalidDepartmentNameException

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
email_adapter = TypeAdapter(EmailStr)

class UserService:

    @staticmethod
    def create_user(user_data, db):
        department_by_name = Department_Repository.get_department_id_by_name(
            user_data.department_name.title(),
            db
        )

        if not department_by_name:
            raise InvalidDepartmentNameException(user_data.department_name)

        try:
            valid_email = email_adapter.validate_python(user_data.email)
        except :
            raise InvalidEmailException()

        is_duplicate_email = UserRepository._validate_is_duplicate_email(valid_email, db)

        if is_duplicate_email:
            raise EmailAlreadyRegisteredException(valid_email)

        user_password = password_hash.hash(user_data.password)
        new_user_valid_data = User(
                    id=user_data.id,
                    username=user_data.username,
                    first_name =user_data.first_name,
                    last_name = user_data.last_name,
                    email = valid_email,
                    department_id = department_by_name.id,
                    password = user_password
                )

        return UserRepository.create_user(new_user_valid_data, db)


