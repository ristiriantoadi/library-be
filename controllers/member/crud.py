from datetime import date, datetime

from config.mongo_collection import MEMBER
from controllers.util.crud import insert_on_db
from models.default.auth import TokenData
from models.member.member import Member
from models.member.util import Gender, Status


async def insert_member_to_db(
    name: str,
    noId: str,
    date: date,
    email: str,
    gender: Gender,
    phoneNumber: str,
    profilePicture: str,
    currentUser: TokenData,
):
    member = Member(
        creatorId=currentUser.userId,
        createTime=datetime.utcnow(),
        name=name,
        noId=noId,
        date=date,
        email=email,
        phoneNumber=phoneNumber,
        profilePicture=profilePicture,
        gender=gender,
        status=Status.ACTIVE,
    )
    member = await insert_on_db(collection=MEMBER, data=member.model_dump())
    return member
