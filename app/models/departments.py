from app.core.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    head_of_department = Column(String)

    books = relationship(
        "Book",                 # model name
        back_populates="department"      # table nmae
    )

    users = relationship(
        "User",
        back_populates="department"
    )
