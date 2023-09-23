from config.mongo_collection import BORROW
from controllers.util.crud import get_list_on_db


async def get_list_borrows(criteria: dict):
    borrows = await get_list_on_db(collection=BORROW, criteria=criteria)
    return borrows
