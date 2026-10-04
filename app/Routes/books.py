from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.books import BookService
from app.schemas.books import BookResponse


router = APIRouter(
    prefix='/book',
    tags=['book'],
)

@router.get('/get', response_model=list[BookResponse])
async def get_all_book(db: Session = Depends(get_db)):
    return BookService.get_all_book(db)


@router.get('/by_id',response_model=BookResponse)
async def get_book_by_id(book_id : int, db: Session = Depends(get_db)):
    return BookService.get_book_by_id(book_id, db)


@router.get('/by_name',response_model=BookResponse)
async def get_book_by_name(book_name : str, db: Session = Depends(get_db)):
    return BookService.get_book_by_name(book_name, db)


@router.get('/available_copy')
async def get_available_copy(book_name : str, db: Session = Depends(get_db)) -> int:
    return BookService.get_available_copy(book_name, db)

@router.get('/by_department',response_model=list[BookResponse])
async def get_book_by_department(department_id : int, db: Session = Depends(get_db)):
    return BookService.get_book_by_department_id(department_id, db)

