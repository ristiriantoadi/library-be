from pydantic import BaseModel

from models.admin.util import AdminRole


class InputAdmin(BaseModel):
    name: str
    noId: str
    role: AdminRole
