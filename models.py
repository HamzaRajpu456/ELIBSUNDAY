from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    __name__ = 'books'
    id: Optional[int] = Field(default= None, primary_key=True)
    book_name: str
    book_author: str
    book_genre: str
    book_summary: str
    book_publish_year: datetime
    book_thumbnail_url: str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class User(SQLModel, table=True):
    __name__ = 'users'
    id : Optional[int] = Field(default=None, primary_key=True)
    user_name : str
    user_email : str
    user_password : str
    user_contact : str
    user_avatar : str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    last_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class BookUpdate(Book):
    book_name: Optional[str] = None
    book_author: Optional[str] = None
    book_genre: Optional[str] = None
    book_summary: Optional[str] = None
    book_publish_year: Optional[datetime] = None
    book_thumbnail_url: Optional[str] = None
    last_edited: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=False)