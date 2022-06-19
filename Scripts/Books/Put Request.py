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

@app.post('/')
async def create_book(book_title,book_author):
    book_max_num = 0
    for key in BOOKS:
        book_num = int(key.split('_')[-1])
        if book_num > book_max_num:
            book_max_num = book_num
    BOOKS[f'book_{book_max_num + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{book_max_num + 1}']

@app.get('/{bookname}')
async def get_book(bookname: str):
    return BOOKS[bookname]

@app.put('/{book_id}')
async def update_book(book_id: str,book_title: str,book_author: str) -> dict:
    book_details = {'title': book_title, 'author': book_author}
    BOOKS[book_id] = book_details
    return book_details