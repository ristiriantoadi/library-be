from config.mongo_collection import BOOK
from controllers.util.crud import get_list_on_db, insert_on_db, update_on_db
from models.book.book import Book
from models.default.auth import TokenData


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


async def get_list_book_on_db():
    return await get_list_on_db(sort="createTime", dir=-1, collection=BOOK)


async def update_book_on_db(criteria: dict, data: dict, currentUser: TokenData):
    await update_on_db(
        collection=BOOK, updateData=data, currentUser=currentUser, criteria=criteria
    )
