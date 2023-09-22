from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel, Field



class OutputBook(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    createTime: datetime
    title: str
    isbn: str
    author: str
    publicationYear: int
    publisher: str
    category: str
    stock: int
    cover: str


# class OutputBookPage(DefaultPage):
#     id: PydanticObjectId = Field(alias="_id")
#     createTime: datetime
#     title: str
#     isbn: str
#     author: str
#     publicationYear: int
#     publisher: str
#     category: str
#     stock: int
#     cover: str
