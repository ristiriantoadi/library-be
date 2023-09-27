from datetime import date, datetime

from fastapi import HTTPException

from config.mongo_collection import MEMBER
from controllers.util.crud import (
    delete_on_db,
    find_on_db,
    get_list_on_db,
    insert_on_db,
    update_on_db,
)
from models.default.auth import TokenData
from models.member.member import Member
from models.member.util import Gender, Status


async def find_member_on_db(criteria):
    return await find_on_db(collection=MEMBER, criteria=criteria)


async def find_member(criteria):
    member = await find_on_db(collection=MEMBER, criteria=criteria)
    if member is None:
        raise HTTPException(status_code=404, detail="Member tidak ditemukan")


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
        date=datetime.combine(date, datetime.min.time()),
        email=email,
        phoneNumber=phoneNumber,
        profilePicture=profilePicture,
        gender=gender,
        status=Status.ACTIVE,
    )
    member = await insert_on_db(
        collection=MEMBER, data=member.model_dump(exclude_none=True)
    )
    return member


async def get_list_member_on_db():
    return await get_list_on_db(
        sort="createTime", dir=-1, collection=MEMBER, criteria={}
    )


async def update_member_on_db(criteria: dict, updateData: dict, currentUser: TokenData):
    await update_on_db(
        collection=MEMBER,
        criteria=criteria,
        updateData=updateData,
        currentUser=currentUser,
    )


async def delete_member_on_db(criteria: dict, currentUser: TokenData):
    await delete_on_db(collection=MEMBER, criteria=criteria, currentUser=currentUser)
