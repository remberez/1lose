from typing import Annotated
from typing import TYPE_CHECKING

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.game import GameCreateSchema, GameReadSchema, GameUpdateSchema
from core.schema.user import UserReadSchema
from .dependencies.auth.current_user import current_user
from .dependencies.services.game import get_game_service

if TYPE_CHECKING:
    from core.service.game import GameService

router = APIRouter(prefix=settings.api.games, tags=["Games"])


@router.post("/", response_model=GameReadSchema)
async def create_game(
        game: GameCreateSchema,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.create(game=game, user_id=user.id)


@router.get("/", response_model=list[GameReadSchema])
async def list_games(
        service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.list()


@router.delete("/{game_id}", response_model=None)
async def delete_game(
        user: Annotated[UserReadSchema, Depends(current_user)],
        game_id: int,
        service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.delete(game_id=game_id, user_id=user.id)

@router.get("/{game_id}", response_model=GameReadSchema)
async def get_game(
        game_id: int,
        service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.get(game_id=game_id)


@router.patch("/{game_id}", response_model=GameReadSchema)
async def update_game(
        game_id: int,
        game: GameUpdateSchema,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated["GameService", Depends(get_game_service)],
):
    return await service.update(game_id=game_id, user_id=user.id, **game.model_dump(exclude_none=True))
