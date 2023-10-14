from datetime import datetime
from typing import List

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from models.borrow.borrow import BorrowStatus
from models.fee.fee_dto import InputFee


class Member(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    name: str
    noId: str


class Book(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    title: str
    isbn: str
    author: str
    publisher: str
    cover: str


class OutputBorrows(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    createTime: datetime
    status: str
    member: Member = None
    book: Book = None


class InputReturnBorrow(BaseModel):
    borrowId: str
    bookId: str
    status: BorrowStatus
    fees: List[InputFee]
