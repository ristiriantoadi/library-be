from fastapi import APIRouter, Depends

from controllers.admin.auth import get_current_user_admin
from models.default.auth import TokenData
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
