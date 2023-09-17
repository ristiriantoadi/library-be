from datetime import date

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from models.member.util import Gender, Status


class OutputMember(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    name: str
    noId: str
    date: date
    gender: Gender
    email: str
    phoneNumber: str
    profilePicture: str
    status: Status
