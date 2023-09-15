from passlib.context import CryptContext

PWDCONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
