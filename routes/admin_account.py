from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from controllers.admin.auth import authenticate_admin, create_token_for_admin

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
