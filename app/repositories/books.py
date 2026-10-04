
from sqlalchemy.orm import Session
from app.models.books import Book
from app.schemas.books import BookCreate

class BookRepository:

    @staticmethod
    def get_all_book(db: Session):
        book_list = db.query(Book).order_by(Book.id).all()
        return book_list


    @staticmethod
    def get_book_by_id(book_id, db:Session):
        return (db.query(Book).
                filter(book_id == Book.id).first())


    @staticmethod
    def get_book_by_name(book_name, db: Session):
        return (db.query(Book).
                filter(book_name == Book.name).first())



    @staticmethod
    def get_book_by_department_id(department_id: int, db:Session):
        return (db.query(Book).
                filter(Book.department_id == department_id).
                order_by(Book.id).all())

