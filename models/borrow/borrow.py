from enum import Enum


from models.default.base import DefaultModel


class BorrowStatus(str, Enum):
    ON_BORROW = "Sedang Dipinjam"
    RETURNED = "Telah Dikembalikan"
    LOST = "Hilang"


class Borrow(DefaultModel):
    bookId: str
    userId: str
    status: BorrowStatus = BorrowStatus.ON_BORROW
