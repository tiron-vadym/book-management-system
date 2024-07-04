# Book Management System

This is a basic web application for managing a collection of books. It allows users to perform CRUD (Create, Read, Update, Delete) operations on books via a web interface.

## Technologies Used:
- Python
- FastAPI (Python web framework)
- SQLAlchemy (Python SQL toolkit and ORM)
- SQLite (Database)
- Jinja2 (Template engine)
- HTML/CSS/JavaScript (Frontend)

## Setup:
### Clone the repository:
```bash
git clone https://github.com/tiron-vadym/test-skills.git
cd test-skills

Set up virtual environment:
python -m venv .venv
- On Windows
.venv\Scripts\activate
- On macOS/Linux
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Initialize the database:
alembic upgrade head

Run the application:
uvicorn main:app --reload

The application will be accessible at http://localhost:8000.

Usage:
- Navigate to http://localhost:8000 in your web browser to access the Book Management System.
- You can view the list of books, add new books, update existing books, and delete books using the web interface.

API Documentation:
The application provides the following API endpoints:
- POST /books: Add a new book.
- GET /books: Retrieve a list of all books.
- GET /books/{book_id}: Retrieve details of a specific book by ID.
- PUT /books/{book_id}: Update an existing book by ID.
- DELETE /books/{book_id}: Delete a book by ID.
