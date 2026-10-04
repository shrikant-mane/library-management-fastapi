from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

from app.core.database import get_db
from app.models.admin import Admin
from app.security.auth import (
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags= ["Authentication"]
)

@router.post("/login")
def admin_login(
    form_data: Annotated[
        OAuth2PasswordRequestForm,
        Depends()
    ],
    db: Session = Depends(get_db)
):

    # 1. Find admin using the username
    admin = db.query(Admin).filter(
        Admin.username == form_data.username
    ).first()

    # 2. Validate username and password
    if admin is None or not verify_password(
        form_data.password,
        admin.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # 3. Generate JWT for the authenticated admin
    access_token = create_access_token(
        admin_id=admin.id
    )

    # 4. Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

