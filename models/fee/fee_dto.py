from datetime import datetime

from pydantic import BaseModel

from models.fee.fee import FeeType


class InputFee(BaseModel):
    feeType: FeeType
    amount: int


class OutputFee(BaseModel):
    createTime: datetime
    amount: int
    feeType: FeeType
