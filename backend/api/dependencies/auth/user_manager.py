from fastapi.params import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from typing_extensions import Annotated, AsyncGenerator

from core.auth.user_manager import UserManager
from .users import get_users_db


async def get_user_manager(
    user_db: Annotated[SQLAlchemyUserDatabase, Depends(get_users_db)],
) -> AsyncGenerator[UserManager, None]:
    # Зависимость для получения менеджера для управления пользователями.
    yield UserManager(user_db)
