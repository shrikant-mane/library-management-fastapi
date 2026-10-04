from fastapi import Request
from fastapi.responses import JSONResponse

from .admin_exception import (EmptyAdminTableException,
                                            AdminDoesNotExistException)


from .department_exceptions import  (EmptyDepartmentTableException,
                                                   InvalidDepartmentNameException)

from.book_exception import EmptyBookTableException

from .common_exception import (InvalidEmailException, InvalidIdException,
                               EmailAlreadyRegisteredException, EmptyTableException)


# =======================
# Common Exception handler
# =======================

async def  invalid_email_address_handler(
        request: Request,
        exc: InvalidEmailException
):
    return JSONResponse(
        status_code=422,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )


async def  invalid_id_handler(
        request: Request,
        exc: InvalidIdException
):
    return JSONResponse(
        status_code=422,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )


async def  email_already_registered_handler(
        request: Request,
        exc: EmailAlreadyRegisteredException
):
    return JSONResponse(
        status_code=409,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )

async def  empty_table_handler(
        request: Request,
        exc: EmptyTableException
):
    return JSONResponse(
        status_code=409,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )

# =======================
# Admin Exception handler
# =======================

async def empty_admin_table_exception_handler(
        request: Request,
        exc: EmptyAdminTableException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )





async def admin_does_not_exist_exception_handler(
        request: Request,
        exc: AdminDoesNotExistException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )

async def invalid_department_email_address_handler(
        request:Request,
        exc: InvalidEmailException
):

    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )





# =======================
# Department Exception handler
# =======================

async def  empty_department_table_handler(
        request: Request,
        exc: EmptyDepartmentTableException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )


async def invalid_department_name_handler(
        request: Request,
        exc: InvalidDepartmentNameException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )


# =======================
# Book Exception handler
# =======================

async def empty_book_table_exception_handler(
        request: Request,
        exc: EmptyBookTableException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )