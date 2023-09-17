from datetime import date

from fastapi import APIRouter, Depends, File, Form, UploadFile

from controllers.admin.auth import get_current_user_admin
from controllers.member.crud import insert_member_to_db
from models.default.auth import TokenData
from models.member.member_dto import OutputMember
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
    # await upload_profile_picture(profilePicture)
    member = await insert_member_to_db(
        name=name,
        noId=noId,
        date=date,
        email=email,
        phoneNumber=phoneNumber,
        profilePicture="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png",
        gender=gender,
        currentUser=current_user,
    )
    return member