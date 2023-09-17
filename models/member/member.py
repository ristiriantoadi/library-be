from datetime import datetime

from models.default.base import DefaultModel
from models.member.util import Gender


class Member(DefaultModel):
    name: str
    noId: str
    date: datetime
    gender: Gender
    email: str
    phoneNumber: str
    profilePicture: str
