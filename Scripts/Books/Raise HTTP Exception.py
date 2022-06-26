from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(min_length=1, max_length=100, title='Apple')
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            'example': {
                'id': 'b77c7d94-c9e7-4ca2-8687-064f23b49d1b',
                'title': 'Python',
                'author': 'Sivasai',
                'rating': 22
            }
        }


BOOKS = []


@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if not BOOKS:
        create_books_without_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_book = []
        while i <= books_to_return:
            new_book.append(BOOKS[i - 1])
            i += 1
        return new_book
    return BOOKS


@app.get('/book/{book_id}')
async def get_book_by_id(book_id: UUID):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise raise_item_cannot_be_found_exception()

@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_cannot_be_found_exception()


@app.delete('/{book_id}')
async def delete_book(book_id: UUID):
    counter = 0

    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            del BOOKS[counter - 1]
            return f'ID: {book_id} deleted'

    raise raise_item_cannot_be_found_exception()


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_without_api():
    book1 = Book(id='a77c7d94-c9e7-4ca2-8687-064f23b49d1b',
                 title='Python',
                 author='Sivasai',
                 description='Python Book',
                 rating=100)
    book2 = Book(id='b77c7d94-c9e7-4ca2-8687-064f23b49d1b',
                 title='Python1',
                 author='Sivasai1',
                 description='Python Book1',
                 rating=99)
    BOOKS.append(book1)
    BOOKS.append(book2)


def raise_item_cannot_be_found_exception():
    raise HTTPException(status_code=404,
                        detail='UUID not fount',
                        headers={'x-header-error': 'Nothing to be seen at the UUID'})