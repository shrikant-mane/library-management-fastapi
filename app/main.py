from fastapi import FastAPI
from .Routes import check, departments
from app.exceptions.department_exceptions import InvalidEmailException
from app.exceptions.handler import invalid_email_address_handler

app = FastAPI()

@app.get('/health')
async def health_check():
    return {'status': 'healthy'}

app.include_router(check.router)
app.include_router(departments.router)
app.add_exception_handler(
    InvalidEmailException,
    invalid_email_address_handler,
)