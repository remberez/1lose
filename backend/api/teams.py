from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.team import EATeamReadSchema
from core.service.team import EATeamService
from .dependencies.services.team import get_ea_team_service

router = APIRouter(prefix=settings.api.teams)


@router.get("/", response_model=list[EATeamReadSchema])
async def list_team(
        service: Annotated[EATeamService, Depends(get_ea_team_service)],
):
    return await service.list()
