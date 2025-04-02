from typing_extensions import TypeVar

from core.repository.user import AbstractUserRepository

UserModelT = TypeVar("UserModelT")


class UserService:
    def __init__(self, repository: AbstractUserRepository):
        self._repository = repository

    async def get(self, user_id: int) -> UserModelT:
        return await self._repository.get(user_id)
