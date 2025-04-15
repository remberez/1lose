from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.business_settings import (
    BusinessSettingsReadSchema,
    BusinessSettingsUpdateSchema,
    BusinessSettingsCreateSchema
)
from core.schema.user import UserReadSchema
from core.service.business_settings import BusinessSettingsService
from .dependencies.auth.current_user import current_user
from .dependencies.services.business_settings import business_settings

router = APIRouter(prefix=settings.api.business, tags=["Business settings"])


@router.get("/{settings_name}", response_model=BusinessSettingsReadSchema)
async def get_settings(
        settings_name: str,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.get(settings_name, user.id)


@router.post("/", response_model=BusinessSettingsReadSchema)
async def create_settings(
        settings_data: BusinessSettingsCreateSchema,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.create(user.id, settings_data)


@router.get("/", response_model=list[BusinessSettingsReadSchema])
async def list_settings(
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.list(user.id)


@router.delete("/{settings_name}", status_code=204)
async def delete_settings(
        settings_name: str,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.delete(settings_name, user.id)
