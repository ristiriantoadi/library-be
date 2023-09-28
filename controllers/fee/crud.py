from datetime import datetime

from beanie import PydanticObjectId

from config.mongo_collection import FEE
from controllers.util.crud import insert_on_db
from models.fee.fee import Fee
from models.fee.fee_dto import InputFee


async def insert_fee_on_db(memberId: str, fee: InputFee, bookId: str, borrowId: str):
    data = Fee(
        createTime=datetime.utcnow(),
        userId=PydanticObjectId(memberId),
        bookId=PydanticObjectId(bookId),
        borrowId=PydanticObjectId(borrowId),
        amount=fee.amount,
        feeType=fee.feeType,
    )
    await insert_on_db(collection=FEE, data=data.model_dump())
