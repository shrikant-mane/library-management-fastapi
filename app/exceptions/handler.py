from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.department_exceptions import InvalidEmailException

async def invalid_email_address_handler(
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