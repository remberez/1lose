from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.tournament import (
    TournamentReadSchema,
    TournamentCreateSchema,
    TournamentUpdateSchema,
)
from core.schema.user import UserReadSchema
from core.service.tournament import TournamentService
from .dependencies.auth.current_user import get_current_active_verify_user, CurrentAdminModeratorUser
from .dependencies.services.tournament import get_tournament_service

router = APIRouter(prefix=settings.api.tournament, tags=["Tournaments"])


@router.get("/{tournament_id}", response_model=TournamentReadSchema)
async def get_tournament(
    tournament_id: int,
    service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    return await service.get(tournament_id=tournament_id)


@router.post("/", response_model=TournamentReadSchema)
async def create_tournament(
    tournament: TournamentCreateSchema,
    user: CurrentAdminModeratorUser,
    service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    return await service.create(user_id=user.id, **tournament.model_dump())


@router.get("/", response_model=list[TournamentReadSchema])
async def list_tournament(
    service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    return await service.list()


@router.delete("/{tournament_id}", response_model=None)
async def delete_tournament(
    tournament_id: int,
    user: CurrentAdminModeratorUser,
    service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    await service.delete(user_id=user.id, tournament_id=tournament_id)


@router.patch("/{tournament_id}", response_model=TournamentReadSchema)
async def update_tournament(
    tournament_id: int,
    user: CurrentAdminModeratorUser,
    service: Annotated[TournamentService, Depends(get_tournament_service)],
    tournament: TournamentUpdateSchema,
):
    return await service.update(
        tournament_id=tournament_id,
        user_id=user.id,
        **tournament.model_dump(exclude_none=True),
    )
