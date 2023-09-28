from datetime import datetime
from typing import List

from pydantic import BaseModel

from models.fee.fee_dto import InputFee


class Member(BaseModel):
    name: str
    noId: str


class Book(BaseModel):
    title: str
    isbn: str
    author: str
    publisher: str


class OutputBorrows(BaseModel):
    createTime: datetime
    status: str
    member: Member = None
    book: Book = None


class InputReturnBorrow(BaseModel):
    borrowId: str
    bookId: str
    fees: List[InputFee]
