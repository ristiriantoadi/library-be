from datetime import date, datetime
from typing import List

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from models.member.util import Gender, Status


class OutputMember(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    createTime: datetime
    name: str
    noId: str
    date: date
    gender: Gender
    email: str
    phoneNumber: str
    profilePicture: str
    status: Status


class OutputMemberPage(BaseModel):
    content: List[OutputMember] = []
