from fastapi import HTTPException
from app.exceptions.common_exception  import InvalidIdException, EmptyTableException
from app.exceptions.book_exception import EmptyBookTableException

from app.repositories.books import BookRepository

class BookService:
    name="Book"

    @ staticmethod
    def get_all_book(db):
        book_list =  BookRepository.get_all_book(db)
        if not book_list:
            raise EmptyTableException(BookService.name)
        else:
            return book_list


    @staticmethod
    def get_book_by_id(book_id, db):
        book = BookRepository.get_book_by_id(book_id, db)
        if not book:
            raise InvalidIdException(BookService.name, book_id)
        else:
            return book


    @staticmethod
    def get_book_by_name(book_name, db):
        name = book_name.title()
        book = BookRepository.get_book_by_name(name, db)
        if not book:
            raise HTTPException(
                status_code=404,
                detail=f"Invalid book name : {name}"
            )
        else:
            return book


    @staticmethod
    def get_available_copy(book_name, db):
        name = book_name.title()
        book = BookRepository.get_book_by_name(name, db)
        if not book:
            raise HTTPException(
                status_code=404,
                detail=f"{name} Book is not available"
            )
        else:
            return book.available_copy

    @staticmethod
    def get_book_by_department_id(department_id, db):
        book_list = BookRepository.get_book_by_department_id(department_id, db)
        if not book_list:
            raise InvalidIdException("Department", department_id)
        else:
            return book_list





