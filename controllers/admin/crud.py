from config.mongo_collection import ADMIN
from controllers.util.crud import insert_on_db


async def insert_admin_on_db(data: dict):
    await insert_on_db(collection=ADMIN, data=data)
