from typing import List

from fastapi import APIRouter, Depends

from controllers.admin.auth import get_current_user_admin
from controllers.borrow.borrow import borrow_book_controller
from controllers.borrow.crud import (
    get_additional_data_borrow,
    get_count_borrows,
    get_list_borrows,
)
from controllers.borrow.filter import get_filter_borrow
from models.borrow.borrow import BorrowStatus
from models.borrow.borrow_dto import OutputBorrows
from models.default.auth import TokenData
from models.util.util_dto import OutputTotalCount

route_admin_borrowing = APIRouter(
    prefix="/admin/borrowing",
    tags=["Admin Borrowing"],
    responses={404: {"description": "Not found"}},
)


@route_admin_borrowing.get("/total_count", response_model=OutputTotalCount)
async def get_total_borrowing_count(
    memberId: str = None,
    status: BorrowStatus = None,
    current_user: TokenData = Depends(get_current_user_admin),
):
    count = await get_count_borrows(
        criteria=get_filter_borrow(memberId=memberId, status=status)
    )
    return OutputTotalCount(count=count)


@route_admin_borrowing.post("/{memberId}")
async def borrow_book(
    memberId: str,
    bookIds: List[str],
    currentUser: TokenData = Depends(get_current_user_admin),
):
    await borrow_book_controller(
        bookIds=bookIds, currentUser=currentUser, memberId=memberId
    )


@route_admin_borrowing.get("", response_model=List[OutputBorrows])
async def get_borrows(
    memberId: str = None,
    status: BorrowStatus = None,
    current_user: TokenData = Depends(get_current_user_admin),
):
    borrows = await get_list_borrows(
        criteria=get_filter_borrow(memberId=memberId, status=status)
    )
    borrows = await get_additional_data_borrow(borrows=borrows["data"])
    print("borrows", borrows)
    return borrows
