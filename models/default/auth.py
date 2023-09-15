from datetime import datetime
from pydantic import BaseModel

from models.user.user import UserType

class TokenData(BaseModel):
    userId: str
    userType: UserType
    exp:datetime