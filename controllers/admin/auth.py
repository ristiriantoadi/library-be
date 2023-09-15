from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt

from config.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from config.mongo_collection import ADMIN
from controllers.util.authentication import PWDCONTEXT
from controllers.util.crud import find_on_db
from models.default.auth import TokenData


async def authenticate_admin(username: str, password: str):
    admin = await find_on_db(collection=ADMIN, criteria={"noId": username.strip()})
    if admin is None:
        raise HTTPException(status_code=401, detail="Username atau password salah")
    if not PWDCONTEXT.verify(password.strip(), admin["credential"]["password"]):
        raise HTTPException(status_code=400, detail="Username atau password salah")
    return admin


def create_token_for_admin(admin: dict):
    data = TokenData(
        userId=str(admin["_id"]),
        exp=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    encoded_jwt = jwt.encode(data.dict(), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
