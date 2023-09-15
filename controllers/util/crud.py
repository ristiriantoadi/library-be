from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection


async def find_on_db(collection: AsyncIOMotorCollection, criteria: dict):
    criteria["isDelete"] = False
    return await collection.find_one(criteria)


async def insert_on_db(collection: AsyncIOMotorCollection, data: dict):
    data["createTime"] = datetime.utcnow()
    await collection.insert_one(data)
