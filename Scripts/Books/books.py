from fastapi import FastAPI
from enum import Enum
app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author one'},
    'book_2': {'title': 'Title Two', 'author': 'Author two'},
    'book_3': {'title': 'Title Three', 'author': 'Author three'},
    'book_4': {'title': 'Title Four', 'author': 'Author four'},
    'book_5': {'title': 'Title Five', 'author': 'Author five'},

}

class DirectionName(str,Enum):
    north = 'North'
    south = 'South'
    east = 'East'
    west = 'West'

@app.get("/")
def read_all_books():
    return BOOKS

@app.get('/book/mybook')
async def read_fav_book():
    return {'book_title': 'My Favorite Book'}

@app.get('/book/{book_id}')
async def get_book(book_id: int):
    return {'book_title' : book_id}

@app.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {'Direction': direction_name,'sub': 'Up'}
    if direction_name == DirectionName.south:
        return {'Direction': direction_name,'sub': 'Down'}
    if direction_name == DirectionName.east:
        return {'Direction': direction_name,'sub': 'Right'}
    return {'Direction': direction_name, 'sub': 'Left'}
