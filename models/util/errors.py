from enum import Enum


class BadRequestException(str, Enum):
    ADMIN_ALREADY_EXIST = "ADMIN_ALREADY_EXIST"


class UnauthorizedException(str, Enum):
    WRONG_USERNAME_OR_PASSWORD = "WRONG_USERNAME_OR_PASSWORD"
