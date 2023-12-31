from datetime import datetime

from config.mongo_collection import FEE
from controllers.util.crud import get_list_on_db, insert_on_db
from models.fee.fee import Fee
from models.fee.fee_dto import InputFee


async def insert_fee_on_db(memberId: str, fee: InputFee, bookId: str, borrowId: str):
    data = Fee(
        createTime=datetime.utcnow(),
        userId=memberId,
        bookId=bookId,
        borrowId=borrowId,
        amount=fee.amount,
        feeType=fee.feeType,
    )
    await insert_on_db(collection=FEE, data=data.dict())


async def get_list_fee_on_db(criteria: dict = {}):
    return await get_list_on_db(
        sort="createTime", dir=-1, collection=FEE, criteria=criteria
    )
