from enum import Enum

from beanie import PydanticObjectId

from models.default.base import DefaultModel


class BorrowStatus(str, Enum):
    ON_BORROW = "Sedang Dipinjam"
    RETURNED = "Telah Dikembalikan"
    LOST = "Hilang"


class Borrow(DefaultModel):
    bookId: PydanticObjectId
    userId: PydanticObjectId
    status: BorrowStatus = BorrowStatus.ON_BORROW
