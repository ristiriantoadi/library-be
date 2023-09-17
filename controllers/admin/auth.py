from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from jose import JWTError, jwt

from config.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from config.mongo_collection import ADMIN
from controllers.util.authentication import PWDCONTEXT, oauth2_scheme_admin
from controllers.util.crud import find_on_db
from models.default.auth import TokenData


async def authenticate_admin(username: str, password: str):
    admin = await find_on_db(collection=ADMIN, criteria={"noId": username.strip()})
    if admin is None:
        raise HTTPException(status_code=401, detail="Username atau password salah")
    if not PWDCONTEXT.verify(password.strip(), admin["credential"]["password"]):
        raise HTTPException(status_code=401, detail="Username atau password salah")
    return admin


def create_token_for_admin(admin: dict):
    data = TokenData(
        userId=str(admin["_id"]),
        exp=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    encoded_jwt = jwt.encode(data.dict(), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user_admin(token: str = Depends(oauth2_scheme_admin)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        tokenData = TokenData(
            userId=payload.get("userId"),
            userType=payload.get("userType"),
            exp=payload.get("exp"),
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return tokenData
