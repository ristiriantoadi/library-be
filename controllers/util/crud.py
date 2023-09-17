from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection


async def find_on_db(collection: AsyncIOMotorCollection, criteria: dict):
    criteria["isDelete"] = False
    return await collection.find_one(criteria)


async def insert_on_db(collection: AsyncIOMotorCollection, data: dict):
    data["createTime"] = datetime.utcnow()
    op = await collection.insert_one(data)
    return await collection.find_one(op.inserted_id)
