from datetime import date, datetime

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, File, Form, UploadFile

from controllers.admin.auth import get_current_user_admin
from controllers.member.count import get_member_count
from controllers.member.crud import (
    delete_member_on_db,
    find_member,
    get_list_member_on_db,
    insert_member_to_db,
    update_member_on_db,
)
from controllers.util.upload_file import upload_file
from models.default.auth import TokenData
from models.member.member_dto import OutputMember, OutputMemberPage
from models.member.util import Gender
from models.util.util_dto import OutputTotalCount

route_admin_member = APIRouter(
    prefix="/admin/member",
    tags=["Admin member"],
    responses={404: {"description": "Not found"}},
)


@route_admin_member.get("/total_count", response_model=OutputTotalCount)
async def get_total_member_count(
    current_user: TokenData = Depends(get_current_user_admin),
):
    count = await get_member_count()
    return OutputTotalCount(count=count)


@route_admin_member.post("/create", response_model=OutputMember)
async def create_member(
    name: str = Form(...),
    noId: str = Form(...),
    date: date = Form(...),
    gender: Gender = Form(...),
    email: str = Form(...),
    phoneNumber: str = Form(...),
    profilePicture: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user_admin),
):
    # await validate_noId_not_exist(noId)
    fileUrl = await upload_file(
        file=profilePicture,
        featureFolder="profile_picture",
    )
    member = await insert_member_to_db(
        name=name,
        noId=noId,
        date=date,
        email=email,
        phoneNumber=phoneNumber,
        profilePicture=fileUrl,
        gender=gender,
        currentUser=current_user,
    )
    return member


@route_admin_member.get("", response_model=OutputMemberPage)
async def get_list_member(
    current_user: TokenData = Depends(get_current_user_admin),
):
    res = await get_list_member_on_db()
    return OutputMemberPage(
        content=res["data"],
    )


@route_admin_member.put("/{idMember}")
async def edit_member(
    idMember: str,
    name: str = Form(...),
    noId: str = Form(...),
    date: date = Form(...),
    gender: Gender = Form(...),
    email: str = Form(...),
    phoneNumber: str = Form(...),
    profilePicture: UploadFile = File(None),
    current_user: TokenData = Depends(get_current_user_admin),
):
    updateData = {
        "name": name,
        "noId": noId,
        "date": datetime.combine(date, datetime.min.time()),
        "gender": gender,
        "email": email,
        "phoneNumber": phoneNumber,
    }
    if profilePicture:
        fileUrl = await upload_file(
            file=profilePicture,
            featureFolder="profile_picture",
        )
        updateData["profilePicture"] = fileUrl
    await update_member_on_db(
        criteria={"_id": PydanticObjectId(idMember)},
        updateData=updateData,
        currentUser=current_user,
    )


@route_admin_member.delete("/{idMember}")
async def delete_member(
    idMember: str,
    currentUser: TokenData = Depends(get_current_user_admin),
):
    await find_member({"_id": PydanticObjectId(idMember)})
    await delete_member_on_db(
        criteria={"_id": PydanticObjectId(idMember)}, currentUser=currentUser
    )
