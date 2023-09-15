from pydantic import BaseModel

from models.admin.util import AdminRole
from models.default.base import DefaultModel


class Credential(BaseModel):
    password: str


class Admin(DefaultModel):
    name: str
    noId: str
    role: AdminRole
    credential: Credential
