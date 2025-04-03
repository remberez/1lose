from typing import Annotated
from typing import TYPE_CHECKING

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.game import GameCreateSchema, GameReadSchema
from core.schema.user import UserReadSchema
from .dependencies.auth.current_user import current_user
from .dependencies.services.game import get_game_service

if TYPE_CHECKING:
    from core.service.game import GameService

router = APIRouter(prefix=settings.api.games)


@router.post("/", response_model=GameReadSchema)
async def create_game(
    game: GameCreateSchema,
    user: Annotated[UserReadSchema, Depends(current_user)],
    service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.create(game=game, user_id=user.id)
