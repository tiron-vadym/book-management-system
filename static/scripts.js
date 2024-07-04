async function addBook(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const published_date = document.getElementById('published_date').value;
    const isbn = document.getElementById('isbn').value;
    const pages = document.getElementById('pages').value;

    const response = await fetch('/books/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, author, published_date, isbn, pages }),
    });

    if (response.ok) {
        window.location.reload();
    }
}

async function getBookDetails(bookId) {
    const response = await fetch(`/books/${bookId}/`);
    const book = await response.json();
    console.log(book);
}

async function deleteBook(bookId) {
    const response = await fetch(`/books/${bookId}/`, {
        method: 'DELETE',
    });

    if (response.ok) {
        window.location.reload();
    }
}

async function updateBook(event, bookId) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const published_date = document.getElementById('published_date').value;
    const isbn = document.getElementById('isbn').value;
    const pages = document.getElementById('pages').value;

    const response = await fetch(`/books/${bookId}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, author, published_date, isbn, pages }),
    });

    if (response.ok) {
        window.location.href = `/books/${bookId}/`;
    }
}
