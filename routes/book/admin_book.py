from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, File, Form, UploadFile

from controllers.admin.auth import get_current_user_admin
from controllers.book.count import get_book_count
from controllers.book.crud import (
    delete_book_on_db,
    find_book,
    get_list_book_on_db,
    insert_book_on_db,
    update_book_on_db,
)
from controllers.book.validation import (
    validate_isbn_unique,
    validate_isbn_unique_on_update,
)
from controllers.borrow.crud import get_list_borrows
from controllers.util.upload_file import upload_file
from models.book.book_dto import OutputBook
from models.default.auth import TokenData
from models.util.util_dto import OutputTotalCount

route_admin_book = APIRouter(
    prefix="/admin/book",
    tags=["Admin Book"],
    responses={404: {"description": "Not found"}},
)


@route_admin_book.get("/categories")
async def get_book_categories(
    current_user: TokenData = Depends(get_current_user_admin),
):
    return [
        "Sastra",
        "Sains",
        "Biografi",
        "Sejarah",
        "Agama",
        "Seni Rupa",
        "Ekonomi dan Bisnis",
    ]


@route_admin_book.get("/total_count", response_model=OutputTotalCount)
async def get_total_book_count(
    current_user: TokenData = Depends(get_current_user_admin),
):
    count = await get_book_count()
    return OutputTotalCount(count=count)


@route_admin_book.post("")
async def add_book(
    title: str = Form(...),
    isbn: str = Form(...),
    author: str = Form(...),
    publicationYear: int = Form(...),
    publisher: str = Form(...),
    category: str = Form(...),
    stock: int = Form(...),
    cover: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user_admin),
):
    await validate_isbn_unique(isbn)
    url = await upload_file(
        file=cover,
        featureFolder="cover",
    )
    await insert_book_on_db(
        title=title,
        isbn=isbn,
        author=author,
        publicationYear=publicationYear,
        publisher=publisher,
        category=category,
        stock=stock,
        cover=url,
    )


@route_admin_book.get("", response_model=List[OutputBook])
async def get_list_book(
    current_user: TokenData = Depends(get_current_user_admin),
):
    res = await get_list_book_on_db()
    print("books", res["data"])
    return res["data"]


@route_admin_book.get("/unborrowed/{memberId}", response_model=List[OutputBook])
async def get_list_unborrowed_books(
    memberId: str,
    current_user: TokenData = Depends(get_current_user_admin),
):
    borrows = await get_list_borrows(criteria={"userId": memberId})
    books = await get_list_book_on_db(
        criteria={
            "_id": {
                "$nin": [
                    PydanticObjectId(borrow["bookId"]) for borrow in borrows["data"]
                ]
            },
            "stock": {"$gt": 0},
        }
    )
    return books["data"]


@route_admin_book.put("/{bookId}")
async def updateBook(
    bookId: str,
    title: str = Form(...),
    isbn: str = Form(...),
    author: str = Form(...),
    publicationYear: int = Form(...),
    publisher: str = Form(...),
    category: str = Form(...),
    stock: int = Form(...),
    cover: UploadFile = File(None),
    currentUser: TokenData = Depends(get_current_user_admin),
):
    await validate_isbn_unique_on_update(isbn=isbn, id=bookId)
    updateData = {
        "title": title,
        "isbn": isbn,
        "author": author,
        "publicationYear": publicationYear,
        "publisher": publisher,
        "category": category,
        "stock": stock,
    }
    if cover:
        fileUrl = await upload_file(
            file=cover,
            featureFolder="cover",
        )
        updateData["cover"] = fileUrl
    await update_book_on_db(
        criteria={"_id": PydanticObjectId(bookId)},
        data=updateData,
        currentUser=currentUser,
    )


@route_admin_book.delete("/{bookId}")
async def delete_book(
    bookId: str,
    currentUser: TokenData = Depends(get_current_user_admin),
):
    await find_book({"_id": PydanticObjectId(bookId)})
    await delete_book_on_db(
        criteria={"_id": PydanticObjectId(bookId)}, currentUser=currentUser
    )
