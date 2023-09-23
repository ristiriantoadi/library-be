from datetime import datetime

from pydantic import BaseModel


class Member(BaseModel):
    name: str
    noId: str


class Book(BaseModel):
    title: str
    isbn: str


class OutputBorrows(BaseModel):
    createTime: datetime
    status: str
    member: Member = None
    book: Book = None
