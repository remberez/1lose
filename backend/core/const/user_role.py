from enum import Enum


class UserRoleCodes(Enum):
    ADMIN: str = "admin"
    MODERATOR: str = "moderator"
    USER: str = "user"
