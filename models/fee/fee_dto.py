from pydantic import BaseModel

from models.fee.fee import FeeType


class InputFee(BaseModel):
    feeType: FeeType
    amount: int
