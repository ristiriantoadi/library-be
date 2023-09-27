from config.mongo_collection import MEMBER
from controllers.util.crud import get_count_on_db


async def get_member_count(criteria: dict = {}):
    count = await get_count_on_db(collection=MEMBER)
    return count


async def get_all_member_count_include_deleted():
    return await MEMBER.count_documents({})
