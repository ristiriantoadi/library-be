from beanie import PydanticObjectId
from fastapi import HTTPException

from config.mongo_collection import ADMIN
from controllers.util.crud import find_on_db, insert_on_db


async def insert_admin_on_db(data: dict):
    await insert_on_db(collection=ADMIN, data=data)


async def get_admin_by_user_id(userId: str):
    admin = await find_on_db(
        collection=ADMIN, criteria={"_id": PydanticObjectId(userId)}
    )
    if admin is None:
        raise HTTPException(status_code=404, detail="Admin tidak ditemukan")
    return admin
