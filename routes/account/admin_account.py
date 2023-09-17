from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from controllers.admin.auth import (
    authenticate_admin,
    create_token_for_admin,
    get_current_user_admin,
)
from controllers.admin.crud import get_admin_by_user_id
from models.default.auth import TokenData
from models.default.auth_dto import OutputCheckToken

route_admin_account = APIRouter(
    prefix="/admin/account",
    tags=["Admin Account"],
    responses={404: {"description": "Not found"}},
)


@route_admin_account.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    admin = await authenticate_admin(
        username=form_data.username, password=form_data.password
    )
    access_token = create_token_for_admin(admin=admin)
    return {"access_token": access_token, "token_type": "bearer"}


@route_admin_account.get("/check_token", response_model=OutputCheckToken)
async def check_token(current_user: TokenData = Depends(get_current_user_admin)):
    user = await get_admin_by_user_id(current_user.userId)
    return user
