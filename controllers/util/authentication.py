from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

PWDCONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme_admin = OAuth2PasswordBearer(
    tokenUrl="admin/account/login", scheme_name="admin_oauth2_schema"
)
