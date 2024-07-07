from fastapi import APIRouter, HTTPException
from models import Book, User, BookUpdate
from constants import DATABASE_URL
from sqlmodel import create_engine, SQLModel, Session, select

# define Database
engine = create_engine(DATABASE_URL)

# Add data to database
SQLModel.metadata.create_all(engine)

books_router = APIRouter()


@books_router.get('/')
async def root():
    return {'message': 'Api running successfully'}


@books_router.get('/books')
async def access_books():
    with Session(engine) as session:
        statement = select(Book)
        books = session.exec(statement).all()
        return {'books': books}


@books_router.get('/books/{book_id}')
async def one_book(book_id: int):
    with Session(engine) as session:
        # we select book from table on behalf of model
        statement = select(Book).where(Book.id == book_id)
        book = session.exec(statement).one()
        print(book)
        return {'book': book}


@books_router.post('/books')
async def create_book(book_data: Book):
    print(book_data)
    # session is an instance of sqlModel session object
    with Session(engine) as session:
        session.add(book_data)
        session.commit()
        session.refresh(book_data)

    return {'message': 'new book created successfully', 'book_data': book_data}


@books_router.put('/books/{book_id}')
async def update_new_book(book_id: int, updated_book: Book):
    with Session(engine) as session:
        statement = select(Book).where(Book.id == book_id)
        existing_book = session.exec(statement).one()
        for key, value in updated_book.dict(exclude_unset=True).items():
            setattr(existing_book, key, value)
        session.add(existing_book)
        session.commit()
        session.refresh(existing_book)
        print('update_book', existing_book)
        return {'message': 'book updated successfully', 'new_book': existing_book}


@books_router.delete('/book/{book_id}')
async def remove_book(book_id: int):
    with Session(engine) as session:
        statement = select(Book).where(Book.id == book_id)
        delete_book = session.exec(statement).one()

        session.delete(delete_book)
        session.commit()
        print('delete_book', delete_book)
        return {'message': 'book deleted successfully', 'delete_book': delete_book}
