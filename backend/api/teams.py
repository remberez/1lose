from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.team import EATeamReadSchema, EATeamCreateSchema
from core.schema.user import UserReadSchema
from core.service.team import EATeamService
from .dependencies.services.team import get_ea_team_service
from .dependencies.auth.current_user import current_user

router = APIRouter(prefix=settings.api.teams, tags=["EA-Teams"])


@router.get("/", response_model=list[EATeamReadSchema])
async def list_team(
        service: Annotated[EATeamService, Depends(get_ea_team_service)],
):
    return await service.list()


@router.post("/", response_model=EATeamReadSchema)
async def create_team(
        service: Annotated[EATeamService, Depends(get_ea_team_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
        team: EATeamCreateSchema,
):
    return await service.create(user_id=user.id, **team.model_dump())


@router.get("/{team_id}", response_model=EATeamReadSchema)
async def get_team(
        team_id: int,
        service: Annotated[EATeamService, Depends(get_ea_team_service)],
):
    return await service.get(team_id=team_id)


@router.delete("/{team_id}", response_model=None)
async def delete_team(
        team_id: int,
        service: Annotated[EATeamService, Depends(get_ea_team_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
):
    return await service.delete(team_id=team_id, user_id=user.id)
