from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The Web Socket Handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head First JavaScript",
        "author": "Hellen Smith",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures in Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T. Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-01-21",
        "page_count": 3006,
        "language": "English",
    },
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books


@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_books(book_data:Book):
 new_book = book_data.model_dump()

 books.append(new_book)

 return new_book

@app.get('/book/{book_id}')
async def get_book(book_id:int):
   for book in books:
      if book['id'] == book_id:
         return book
      

   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
       detail = "book NOT found"                
                       )

