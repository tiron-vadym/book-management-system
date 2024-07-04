from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from book_system import crud
from book_system.schemas import BookCreate, BookUpdate
from dependencies import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/books/", response_class=HTMLResponse)
def create_book(request: Request, book: BookCreate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db=db, title=book.title)

    if db_book:
        raise HTTPException(status_code=400, detail="Such name for Book already exists")

    crud.create_book(db=db, book=book)
    books = crud.get_books(db=db)
    return templates.TemplateResponse("book_list.html", {"request": request, "books": books})


@router.get("/books/", response_class=HTMLResponse)
def read_books(request: Request, db: Session = Depends(get_db)):
    books = crud.get_books(db=db)
    return templates.TemplateResponse("book_list.html", {"request": request, "books": books})


@router.get("/books/{book_id}/", response_class=HTMLResponse)
def read_single_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db=db, book_id=book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return templates.TemplateResponse("book_detail.html", {"request": request, "book": book})


@router.put("/books/{book_id}/", response_class=HTMLResponse)
def update_book(request: Request, book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    crud.update_book(db=db, book_id=book_id, book=book)
    updated_book = crud.get_book(db=db, book_id=book_id)
    return templates.TemplateResponse("book_detail.html", {"request": request, "book": updated_book})


@router.delete("/books/{book_id}/", response_class=HTMLResponse)
def delete_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    crud.delete_book(db=db, book_id=book_id)
    books = crud.get_books(db=db)
    return templates.TemplateResponse("book_detail.html", {"request": request, "books": books})
