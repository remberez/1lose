from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.match import MatchReadSchema
from core.service.match import MatchService
from .dependencies.services.match import match_service

router = APIRouter(prefix=settings.api.match, tags=["Matches"])


@router.get("/", response_model=list[MatchReadSchema])
async def list_matches(
        service: Annotated[MatchService, Depends(match_service)],
):
    return await service.list()
