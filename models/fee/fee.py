from enum import Enum

from beanie import PydanticObjectId

from models.default.base import DefaultModel


class FeeType(str, Enum):
    LATE_RETURN = "Keterlambatan"
    LOST_BOOK = "Buku Hilang"
    DAMAGE_BOOK = "Buku Rusak"


class Fee(DefaultModel):
    userId: PydanticObjectId
    bookId: PydanticObjectId
    borrowId: PydanticObjectId
    amount: int
    feeType: FeeType
