from fastapi import FastAPI

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
        "publisher": "Packt Publishing",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    }
]


@app.get('/books')
async def get_all_books():
    return books


@app.post('/books')
async def create_a_book() -> dict:
    pass

@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    pass

@app.get('/book/{book_id}')
async def update_book(book_id:int) -> dict:
    pass

@app.get('/book/{book_id}')
async def delete_book(book_id:int) -> dict:
    pass
