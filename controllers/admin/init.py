from config.config import NAME, NO_ID, PASSWORD
from controllers.admin.crud import insert_admin_on_db
from controllers.util.authentication import PWDCONTEXT
from models.admin.admin import Admin
from models.admin.util import AdminRole


async def init_admin():
    admin = Admin(
        name=NAME,
        noId=NO_ID,
        role=AdminRole.SUPERADMIN,
        credential={"password": PWDCONTEXT.encrypt(PASSWORD)},
    )
    await insert_admin_on_db(admin.model_dump())
