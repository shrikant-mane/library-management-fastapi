from fastapi import FastAPI
from .Routes import check, departments,admin
from app.exceptions.department_exceptions import InvalidDepartmentEmailException
from app.exceptions.admin_exception import InvalidADminEmailException
from app.exceptions.handler import invalid_department_email_address_handler, invalid_admin_email_address_handler


app = FastAPI()

@app.get('/health')
async def health_check():
    return {'status': 'healthy'}

app.include_router(check.router)
app.include_router(departments.router)
app.include_router(admin.router)
app.add_exception_handler(
    InvalidDepartmentEmailException,
    invalid_department_email_address_handler,
)

app.add_exception_handler(
    InvalidADminEmailException,
    invalid_admin_email_address_handler,
)