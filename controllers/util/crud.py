import math
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection


async def find_on_db(collection: AsyncIOMotorCollection, criteria: dict):
    criteria["isDelete"] = False
    return await collection.find_one(criteria)


async def insert_on_db(collection: AsyncIOMotorCollection, data: dict):
    data["createTime"] = datetime.utcnow()
    op = await collection.insert_one(data)
    return await collection.find_one(op.inserted_id)


async def get_list_on_db(
    size: int,
    page: int,
    sort: str,
    dir: int,
    collection: AsyncIOMotorCollection,
    criteria: dict,
):
    cursor = collection.find(criteria).skip(page * size).limit(size).sort(sort, dir)
    data = await cursor.to_list(length=size)
    totalElements = await collection.count_documents(criteria)
    return {
        "data": data,
        "totalElements": totalElements,
        "totalPages": math.ceil(totalElements / size),
    }
