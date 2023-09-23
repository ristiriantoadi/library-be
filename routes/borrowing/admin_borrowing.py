from typing import List

from fastapi import APIRouter, Depends

from controllers.admin.auth import get_current_user_admin
from controllers.borrow.borrow import borrow_book_controller
from models.default.auth import TokenData
from models.util.util_dto import OutputTotalCount

route_admin_borrowing = APIRouter(
    prefix="/admin/borrowing",
    tags=["Admin Borrowing"],
    responses={404: {"description": "Not found"}},
)


@route_admin_borrowing.get("/total_count", response_model=OutputTotalCount)
async def get_total_borrowing_count(
    current_user: TokenData = Depends(get_current_user_admin),
):
    return OutputTotalCount(count=0)


@route_admin_borrowing.post("/{memberId}")
async def borrow_book(
    memberId: str,
    bookIds: List[str],
    currentUser: TokenData = Depends(get_current_user_admin),
):
    await borrow_book_controller(
        bookIds=bookIds, currentUser=currentUser, memberId=memberId
    )
