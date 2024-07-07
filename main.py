from fastapi import FastAPI
from constants import version
from books.routes import books_router
# create instance
app = FastAPI()
app.include_router(books_router)
# prefix= f'/api/{version}'