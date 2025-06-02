from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.map import MapReadSchema, MapCreateSchema, MapUpdateSchema
from core.schema.user import UserReadSchema
from core.service.map import MapService
from .dependencies.services.map import map_service
from .dependencies.auth.current_user import get_current_active_verify_user

router = APIRouter(prefix=settings.api.map, tags=["Maps"])


@router.get("/", response_model=list[MapReadSchema])
async def map_list(
        service: Annotated[MapService, Depends(map_service)]
):
    return await service.list()


@router.post("/", response_model=MapReadSchema)
async def create_map(
        user: Annotated[UserReadSchema, Depends(get_current_active_verify_user)],
        service: Annotated[MapService, Depends(map_service)],
        map_data: MapCreateSchema,
):
    return await service.create(user.id, map_data)


@router.get("/{map_id}", response_model=MapReadSchema)
async def get_map(
        map_id: int,
        service: Annotated[MapService, Depends(map_service)],
):
    return await service.get(map_id)


@router.patch("/{map_id}", response_model=MapReadSchema)
async def update_map(
        map_id: int,
        service: Annotated[MapService, Depends(map_service)],
        map_data: MapUpdateSchema,
        user: Annotated[UserReadSchema, Depends(get_current_active_verify_user)],
):
    return await service.update(map_id, user.id, map_data)


@router.delete("/{map_id}")
async def delete_map(
        map_id: int,
        user: Annotated[UserReadSchema, Depends(get_current_active_verify_user)],
        service: Annotated[MapService, Depends(map_service)],
):
    return await service.delete(map_id, user.id)
