from typing import List

from fastapi import APIRouter, Depends

from controllers.admin.auth import get_current_user_admin
from controllers.fee.crud import get_list_fee_on_db
from models.default.auth import TokenData
from models.fee.fee_dto import OutputFee

route_admin_fee = APIRouter(
    prefix="/admin/fee",
    tags=["Admin Fee"],
    responses={404: {"description": "Not found"}},
)


@route_admin_fee.get("", response_model=List[OutputFee])
async def get_fee(
    userId: str,
    current_user: TokenData = Depends(get_current_user_admin),
):
    fees = await get_list_fee_on_db({"userId": userId})
    return fees["data"]
