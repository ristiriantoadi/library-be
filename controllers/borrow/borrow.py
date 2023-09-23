from datetime import datetime
from typing import List

from beanie import PydanticObjectId

from config.mongo_collection import BORROW
from controllers.util.crud import insert_many_on_db
from models.borrow.borrow import Borrow
from models.default.auth import TokenData


async def borrow_book_controller(
    bookIds: List[str], currentUser: TokenData, memberId: str
):
    borrows = []
    for id in bookIds:
        borrow = Borrow(
            creatorId=PydanticObjectId(currentUser.userId),
            createTime=datetime.utcnow(),
            bookId=PydanticObjectId(id),
            userId=PydanticObjectId(memberId),
        )
        borrows.append(borrow.dict())
    await insert_many_on_db(collection=BORROW, data=borrows)
