from typing import Optional
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author one'},
    'book_2': {'title': 'Title Two', 'author': 'Author two'},
    'book_3': {'title': 'Title Three', 'author': 'Author three'},
    'book_4': {'title': 'Title Four', 'author': 'Author four'},
    'book_5': {'title': 'Title Five', 'author': 'Author five'},

}

@app.get("/")
def read_all_books(skip_book: Optional[str]= None):
    if skip_book:
        new_book = BOOKS.copy()
        del new_book[skip_book]
        return new_book
    return BOOKS

@app.get('/{bookname}')
async def get_book(bookname: str):
    return BOOKS[bookname]