from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.user import UserReadSchema
from core.service.business_settings import BusinessSettingsService
from .dependencies.auth.current_user import current_user
from .dependencies.services.business_settings import business_settings

router = APIRouter(prefix=settings.api.business, tags=["Business settings"])


@router.get("/{settings_name}")
async def get_settings(
        settings_name: str,
        user: Annotated[UserReadSchema, Depends(current_user)],
        service: Annotated[BusinessSettingsService, Depends(business_settings)],
):
    return await service.get(settings_name, user.id)
