from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.tournament import TournamentReadSchema, TournamentCreateSchema
from core.schema.user import UserReadSchema
from core.service.tournament import TournamentService
from .dependencies.services.tournament import get_tournament_service
from .dependencies.auth.current_user import current_user

router = APIRouter(prefix=settings.api.tournament)


@router.get("/{tournament_id}", response_model=TournamentReadSchema)
async def get_tournament(
        tournament_id: int,
        service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    return await service.get(tournament_id=tournament_id)


@router.post("/", response_model=TournamentReadSchema)
async def create_tournament(
        tournament: TournamentCreateSchema,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[TournamentService, Depends(get_tournament_service)],
):
    return await service.create(user_id=user.id, **tournament.model_dump())
