from beanie import PydanticObjectId
from fastapi import HTTPException

from controllers.book.crud import find_book_on_db


async def validate_isbn_unique(isbn: str):
    book = await find_book_on_db({"isbn": isbn})
    if book:
        raise HTTPException(status_code=400, detail="Nomor ISBN telah digunakan")


async def validate_isbn_unique_on_update(isbn: str, id: str):
    book = await find_book_on_db({"isbn": isbn, "_id": {"$ne": PydanticObjectId(id)}})
    if book:
        raise HTTPException(status_code=400, detail="Nomor ISBN telah digunakan")
