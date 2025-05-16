from typing import Annotated

from fastapi import APIRouter, Form, UploadFile
from fastapi.params import Depends, File

from core.config import settings
from core.schema.team import EATeamReadSchema, EATeamCreateSchema, EATeamUpdateSchema
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
    name: Annotated[str, Form()],
    game_id: Annotated[int, Form()],
    icon: Annotated[UploadFile, File()],
):
    team = EATeamCreateSchema(name=name, game_id=game_id)
    return await service.create(user_id=user.id, team=team, icon=icon.file)


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


@router.patch("/{team_id}", response_model=EATeamReadSchema)
async def update_team(
    team_id: int,
    service: Annotated[EATeamService, Depends(get_ea_team_service)],
    user: Annotated[UserReadSchema, Depends(current_user)],
    name: Annotated[str | None, Form()] = None,
    game_id: Annotated[int | None, Form()] = None,
    icon: Annotated[UploadFile | None, File()] = None,
):
    team = EATeamUpdateSchema(name=name, game_id=game_id)
    file = icon.file if icon else None
    return await service.update(
        team_id=team_id, user_id=user.id, team=team, icon=file
    )
