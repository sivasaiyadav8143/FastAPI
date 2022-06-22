from typing import Optional

from fastapi import FastAPI
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
            'example' : {
                'id': 'b77c7d94-c9e7-4ca2-8687-064f23b49d1b',
                'title': 'Python',
                'author': 'Sivasai',
                'rating': 22
            }
        }


BOOKS = []


@app.get('/')
async def read_all_books():
    if not BOOKS:
        create_books_without_api()
    return BOOKS


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