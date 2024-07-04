from typing import List

from sqlalchemy.orm import Session

from book_system.models import Book
from book_system.schemas import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(
        title=book.title,
        author=book.author,
        published_date=book.published_date,
        isbn=book.isbn,
        pages=book.pages,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_book(db: Session, book_id: int) -> Book:
    return db.query(Book).filter(Book.id == book_id).first()


def get_book_by_title(db: Session, title: str) -> Book:
    return db.query(Book).filter(Book.title == title).first()


def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[Book]:
    return db.query(Book).offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book: BookUpdate) -> Book:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for key, value in book.dict(exclude_none=True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> None:
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
