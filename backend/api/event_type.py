from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from api.dependencies.auth.current_user import CurrentAdminUser
from api.dependencies.services.event_type import get_event_type_service
from core.config import settings
from core.schema.event_type import EventTypeCreateSchema, EventTypeReadSchema
from core.service.event_type import EventTypeService

router = APIRouter(prefix=settings.api.event_type, tags=["Event type"])


@router.post("/", response_model=EventTypeReadSchema)
async def create_type(
        _: CurrentAdminUser,
        type_data: EventTypeCreateSchema,
        service: Annotated[EventTypeService, Depends(get_event_type_service)]
):
    return await service.create(type_data)


@router.get("/{code}", response_model=EventTypeReadSchema)
async def get_type(
        code: str,
        service: Annotated[EventTypeService, Depends(get_event_type_service)]
):
    return await service.get(code)
