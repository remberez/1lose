from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.business_settings import (
    BusinessSettingsReadSchema,
    BusinessSettingsUpdateSchema,
    BusinessSettingsCreateSchema
)
from core.service.business_settings import BusinessSettingsService
from .dependencies.auth.current_user import CurrentAdminUser
from .dependencies.services.business_settings import business_settings

router = APIRouter(prefix=settings.api.business, tags=["Business settings"])


@router.get("/{settings_name}", response_model=BusinessSettingsReadSchema)
async def get_settings(
        settings_name: str,
        user: CurrentAdminUser,
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.get(settings_name, user.id)


@router.post("/", response_model=BusinessSettingsReadSchema)
async def create_settings(
        settings_data: BusinessSettingsCreateSchema,
        user: CurrentAdminUser,
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.create(user.id, settings_data)


@router.get("/", response_model=list[BusinessSettingsReadSchema])
async def list_settings(
        user: CurrentAdminUser,
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.list(user.id)


@router.delete("/{settings_name}", status_code=204)
async def delete_settings(
        settings_name: str,
        user: CurrentAdminUser,
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.delete(settings_name, user.id)


@router.patch("/{settings_name}", response_model=BusinessSettingsReadSchema)
async def update_settings(
        settings_name: str,
        user: CurrentAdminUser,
        settings_data: BusinessSettingsUpdateSchema,
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.update(settings_name, settings_data, user.id)
