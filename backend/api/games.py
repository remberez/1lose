from typing import Annotated
from typing import TYPE_CHECKING

from fastapi import APIRouter, UploadFile, Form
from fastapi.params import Depends, File

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
    user: Annotated[UserReadSchema, Depends(current_user)],
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    icon: Annotated[UploadFile, File()],
    service: Annotated["GameService", Depends(get_game_service)],
):
    game_data = GameCreateSchema(name=name, description=description)
    return await service.create(game=game_data, user_id=user.id, icon=icon.file)


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
    user: Annotated[UserReadSchema, Depends(current_user)],
    service: Annotated["GameService", Depends(get_game_service)],
    name: Annotated[str | None, Form()] = None,
    description: Annotated[str | None, Form()] = None,
    icon: Annotated[UploadFile | None, File()] = None,
):
    game = GameUpdateSchema(name=name, description=description)
    file = icon.file if icon else None
    return await service.update(
        game_id=game_id,
        user_id=user.id,
        game=game,
        icon=file,
    )
