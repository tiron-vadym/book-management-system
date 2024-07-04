from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
)

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True)
    author = Column(String(255))
    published_date = Column(Date)
    isbn = Column(String(255))
    pages = Column(Integer)
