from functools import wraps
from typing import Callable, TypeVar, Any, Coroutine

from typing_extensions import ParamSpec

from core.const.user_role import UserRoleCodes
from core.exceptions.user_exc import UserPermissionError
from core.repository.user import AbstractUserRepository

UserModelT = TypeVar("UserModelT")
P = ParamSpec('P')
R = TypeVar('R')

class UserService:
    def __init__(self, repository: AbstractUserRepository):
        self._repository = repository

    async def get(self, user_id: int) -> UserModelT:
        return await self._repository.get(user_id)


class UserPermissionsService:
    def __init__(self, user_repository: AbstractUserRepository):
        self._user_repository = user_repository

    def check_admin_or_moderator(
            self,
            func: Callable[P, Coroutine[Any, Any, R]]
    ) -> Callable[P, Coroutine[Any, Any, R]]:
        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Первый аргумент - self (метод класса), второй - user_id
            user_id = kwargs.get('user_id') or args[1] if len(args) > 1 else None

            user = await self._user_repository.get(user_id)
            if user.role_code not in (UserRoleCodes.ADMIN.value, UserRoleCodes.MODERATOR.value):
                raise UserPermissionError()

            return await func(*args, **kwargs)

        return wrapper
