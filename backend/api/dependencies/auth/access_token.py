from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated
from typing_extensions import AsyncGenerator

from core.models import AccessTokenModel
from core.models.db_helper import db_helper


async def get_access_token_db(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> AsyncGenerator[AsyncSession, None]:
    return AccessTokenModel.get_db(session)
