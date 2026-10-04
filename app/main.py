from fastapi import FastAPI
from .Routes import check,admin, user, departments, books, auth
from .exceptions.common_exception import (InvalidEmailException, InvalidIdException,
                                          EmailAlreadyRegisteredException,
                                          EmptyTableException)

from .exceptions.department_exceptions import (EmptyDepartmentTableException,
                                                  InvalidDepartmentNameException)

from .exceptions.admin_exception import (EmptyAdminTableException,
                                            AdminDoesNotExistException)

from .exceptions.book_exception import EmptyBookTableException

from .exceptions.handler import (invalid_email_address_handler,
                                 invalid_id_handler,
                                 email_already_registered_handler,
                                 empty_table_handler,
                                admin_does_not_exist_exception_handler)
from .exceptions.handler import (empty_admin_table_exception_handler,
                                # invalid_department_id_handler,
                                invalid_department_name_handler)

from .exceptions.handler import empty_book_table_exception_handler

app = FastAPI()


@app.get('/health')
async def health_check():
    return {'status': 'healthy'}


app.include_router(check.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)
app.include_router(departments.router)
app.include_router(books.router)


#======================
# Common Exceptions
#======================
app.add_exception_handler(
    InvalidEmailException,
    invalid_email_address_handler,
)

app.add_exception_handler(
    InvalidIdException,
    invalid_id_handler,
)

app.add_exception_handler(
    EmailAlreadyRegisteredException,
    email_already_registered_handler
)

app.add_exception_handler(
    EmptyTableException,
    empty_table_handler
)

#======================
# Admin Exceptions
#======================
app.add_exception_handler(
    EmptyAdminTableException,
    empty_admin_table_exception_handler,
)


app.add_exception_handler(
    AdminDoesNotExistException,
    admin_does_not_exist_exception_handler,
)


#======================
# Department Exceptions
#======================

app.add_exception_handler(
    EmptyDepartmentTableException,
    empty_admin_table_exception_handler,
)



app.add_exception_handler(
    InvalidDepartmentNameException,
    invalid_department_name_handler,
)


#======================
# Book Exceptions
#======================
app.add_exception_handler(
    EmptyBookTableException,
    empty_book_table_exception_handler,
)