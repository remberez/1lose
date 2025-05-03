from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends, Query

from core.config import settings
from core.schema.match import MatchReadSchema, MatchCreateSchema, MatchUpdateSchema, MathFilterSchema
from core.schema.user import UserReadSchema
from core.service.match import MatchService
from .dependencies.auth.current_user import current_user
from .dependencies.services.match import match_service

router = APIRouter(prefix=settings.api.match, tags=["Matches"])


@router.get("/", response_model=list[MatchReadSchema])
async def list_matches(
    service: Annotated[MatchService, Depends(match_service)],
    filters: Annotated[MathFilterSchema, Query()],
):
    return await service.list(filters)


@router.post("/", response_model=MatchReadSchema)
async def create_match(
    user: Annotated[UserReadSchema, Depends(current_user)],
    service: Annotated[MatchService, Depends(match_service)],
    match: MatchCreateSchema,
):
    return await service.create(user_id=user.id, match_data=match)


@router.patch("/{match_id}", response_model=MatchReadSchema)
async def update_match(
    match_id: int,
    match_data: MatchUpdateSchema,
    user: Annotated[UserReadSchema, Depends(current_user)],
    service: Annotated[MatchService, Depends(match_service)],
):
    return await service.update(user.id, match_id, match_data)


@router.delete("/{match_id}")
async def delete_match(
    match_id: int,
    user: Annotated[UserReadSchema, Depends(current_user)],
    service: Annotated[MatchService, Depends(match_service)],
):
    return await service.delete(user.id, match_id)


@router.get("/{match_id}")
async def get_match(
    match_id: int,
    service: Annotated[MatchService, Depends(match_service)],
):
    return await service.get(match_id)
