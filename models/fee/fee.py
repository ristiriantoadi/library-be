from enum import Enum


from models.default.base import DefaultModel


class FeeType(str, Enum):
    LATE_RETURN = "Keterlambatan"
    LOST_BOOK = "Buku Hilang"
    DAMAGE_BOOK = "Buku Rusak"


class Fee(DefaultModel):
    userId: str
    bookId: str
    borrowId: str
    amount: int
    feeType: FeeType
