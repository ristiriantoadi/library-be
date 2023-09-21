from fastapi import APIRouter, Depends, File, Form, UploadFile

from controllers.admin.auth import get_current_user_admin
from controllers.book.crud import insert_book_on_db
from controllers.util.upload_file import upload_file
from models.default.auth import TokenData
from models.util.util_dto import OutputTotalCount

route_admin_book = APIRouter(
    prefix="/admin/book",
    tags=["Admin Book"],
    responses={404: {"description": "Not found"}},
)


@route_admin_book.get("/total_count", response_model=OutputTotalCount)
async def get_total_book_count(
    current_user: TokenData = Depends(get_current_user_admin),
):
    return OutputTotalCount(count=0)


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
