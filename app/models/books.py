from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    author = Column(String,nullable=False)
    isbn = Column(String,unique=True,nullable=False)
    department_id = Column(Integer,ForeignKey("department.id"),nullable=False)
    available_copy = Column(Integer,nullable=False)
    total_copy = Column(Integer,nullable=False)

    department = relationship(
        "Department",
        back_populates="books"
    )


