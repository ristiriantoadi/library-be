from enum import Enum


class BadRequestException(str, Enum):
    ADMIN_ALREADY_EXIST = "ADMIN_ALREADY_EXIST"
