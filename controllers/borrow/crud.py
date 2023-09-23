from config.mongo_collection import BORROW
from controllers.util.crud import get_count_on_db, get_list_on_db


async def get_list_borrows(criteria: dict):
    borrows = await get_list_on_db(collection=BORROW, criteria=criteria)
    return borrows


async def get_count_borrows(criteria: dict):
    return await get_count_on_db(criteria=criteria, collection=BORROW)
