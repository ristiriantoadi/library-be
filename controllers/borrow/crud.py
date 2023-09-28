from typing import List

from beanie import PydanticObjectId

from config.mongo_collection import BORROW
from controllers.book.crud import find_book_on_db
from controllers.member.crud import find_member_on_db
from controllers.util.crud import get_count_on_db, get_list_on_db


async def get_list_borrows(criteria: dict):
    borrows = await get_list_on_db(collection=BORROW, criteria=criteria)
    return borrows


async def get_count_borrows(criteria: dict):
    return await get_count_on_db(criteria=criteria, collection=BORROW)


async def get_additional_data_borrow(borrows: List[dict]):
    for borrow in borrows:
        borrow["member"] = await find_member_on_db(
            {"_id": PydanticObjectId(borrow["userId"])}
        )
        borrow["book"] = await find_book_on_db(
            {"_id": PydanticObjectId(borrow["bookId"])}
        )
    return borrows


async def update_borrow(criteria: dict, update: dict):
    await BORROW.update_one(criteria, update)
