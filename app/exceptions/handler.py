from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.department_exceptions import InvalidDepartmentEmailException
from app.exceptions.admin_exception import InvalidADminEmailException

async def invalid_department_email_address_handler(
        request:Request,
        exc: InvalidDepartmentEmailException
):

    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )


async def  invalid_admin_email_address_handler(
        request: Request,
        exc: InvalidADminEmailException
):
    return JSONResponse(
        status_code=404,
        content={
            'status': 'error',
            'message': exc.msg
        }
    )