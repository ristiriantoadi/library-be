from config.mongo_collection import BOOK
from controllers.util.crud import get_count_on_db


async def get_book_count(criteria: dict = {}):
    return await get_count_on_db(collection=BOOK)
