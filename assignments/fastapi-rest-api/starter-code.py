from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(title="Books REST API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley", year=1818),
}
next_book_id = 3


# Task 1: Implement GET /books and GET /books/{book_id}.


# Task 2: Implement POST /books with HTTP status 201.


# Task 3: Implement PUT /books/{book_id} and DELETE /books/{book_id}.
