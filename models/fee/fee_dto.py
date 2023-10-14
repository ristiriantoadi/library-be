from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from models.fee.fee import FeeType


class InputFee(BaseModel):
    feeType: FeeType
    amount: int


class OutputFee(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    createTime: datetime
    amount: int
    feeType: FeeType
