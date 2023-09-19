from datetime import date

from fastapi import APIRouter, Depends, File, Form, UploadFile

from controllers.admin.auth import get_current_user_admin
from controllers.member.crud import get_list_member_on_db, insert_member_to_db
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
    return OutputTotalCount(count=0)


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
        featureFolder="profile_picture/{userId}".format(userId=current_user.userId),
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
