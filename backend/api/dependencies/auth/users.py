from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated, AsyncGenerator

from core.models import UserModel
from core.models.db_helper import db_helper


async def get_users_db(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> AsyncGenerator[AsyncSession, None]:
    yield UserModel.get_db(session)
