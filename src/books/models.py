from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql import pg
from datetime import datetime
import uuid


class Book(SQLModel, table=True):
        uid: uuid.UUID = Field(
            sa_column=Column(
                    pg.UUID,
            )
        )
        title: str
        author: str
        publisher: str
        published_date: str
        page_count: int
        language: str
        created_at: datetime
        update_at: datetime
