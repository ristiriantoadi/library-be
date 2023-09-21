from config.mongo_collection import BOOK
from controllers.util.crud import insert_on_db
from models.book.book import Book


async def insert_book_on_db(
    title: str,
    isbn: str,
    author: str,
    publicationYear: int,
    publisher: str,
    category: str,
    stock: int,
    cover: str,
):
    book = Book(
        title=title,
        isbn=isbn,
        author=author,
        publicationYear=publicationYear,
        publisher=publisher,
        category=category,
        stock=stock,
        cover=cover,
    )
    await insert_on_db(collection=BOOK, data=book.dict())
