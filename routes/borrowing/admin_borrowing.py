from datetime import datetime
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends

from controllers.admin.auth import get_current_user_admin
from controllers.book.crud import update_book
from controllers.borrow.borrow import borrow_book_controller
from controllers.borrow.crud import (get_additional_data_borrow,
                                     get_count_borrows, get_list_borrows,
                                     update_borrow)
from controllers.borrow.filter import get_filter_borrow
from controllers.fee.crud import insert_fee_on_db
from models.borrow.borrow import BorrowStatus
from models.borrow.borrow_dto import InputReturnBorrow, OutputBorrows
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


@route_admin_borrowing.put("/{memberId}/return")
async def return_borrow_book(
    memberId: str,
    inputs: List[InputReturnBorrow],
    currentUser: TokenData = Depends(get_current_user_admin),
):
    for input in inputs:
        await update_borrow(
            criteria={"_id": PydanticObjectId(input.borrowId)},
            update={
                "$set": {
                    "status": input.status,
                    "updateTime": datetime.utcnow(),
                    "updaterId": currentUser.userId,
                }
            },
        )
        if input.status != BorrowStatus.LOST:
            await update_book(
                criteria={"_id": PydanticObjectId(input.bookId)},
                update={"$inc": {"stock": 1}},
            )
        for fee in input.fees:
            await insert_fee_on_db(
                memberId=memberId, fee=fee, bookId=input.bookId, borrowId=input.borrowId
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
    return borrows
