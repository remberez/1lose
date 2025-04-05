from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.match import MatchReadSchema, MatchCreateSchema
from core.schema.user import UserReadSchema
from core.service.match import MatchService
from .dependencies.services.match import match_service
from .dependencies.auth.current_user import current_user

router = APIRouter(prefix=settings.api.match, tags=["Matches"])


@router.get("/", response_model=list[MatchReadSchema])
async def list_matches(
        service: Annotated[MatchService, Depends(match_service)],
):
    return await service.list()


@router.post("/", response_model=MatchReadSchema)
async def create_match(
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[MatchService, Depends(match_service)],
        match: MatchCreateSchema,
):
    return await service.create(user_id=user.id, match_data=match)

