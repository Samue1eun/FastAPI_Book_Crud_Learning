from pydantic import BaseModel
import uuid

class Book(BaseModel):
        uid: uuid.UUID
        title: str
        author: str
        publisher: str
        published_date: str
        page_count: int
        language: str


class BookUpdateModel(BaseModel):
        title: str
        author: str
        publisher: str
        page_count: int
        language: str
