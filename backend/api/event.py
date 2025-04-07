from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.event import EventReadSchema, EventCreateSchema, EventUpdateSchema
from core.schema.user import UserReadSchema
from core.service.event import EventService
from .dependencies.services.event import event_service
from .dependencies.auth.current_user import current_user

router = APIRouter(prefix=settings.api.event, tags=["Events"])


@router.get("/", response_model=list[EventReadSchema])
async def event_list(
        service: Annotated[EventService, Depends(event_service)],
):
    return await service.list()


@router.post("/", response_model=EventReadSchema)
async def create_event(
        service: Annotated[EventService, Depends(event_service)],
        user: Annotated[UserReadSchema, Depends(current_user)],
        event: EventCreateSchema,
):
    return await service.create(user.id, event)


@router.get("/{event_id}", response_model=EventReadSchema)
async def get_event(
        service: Annotated[EventService, Depends(event_service)],
        event_id: int,
):
    return await service.get(event_id)


@router.patch("/{event_id}", response_model=EventReadSchema)
async def update_event(
        service: Annotated[EventService, Depends(event_service)],
        event_id: int,
        user: Annotated[UserReadSchema, Depends(current_user)],
        event: EventUpdateSchema,
):
    return await service.update(event_id, user.id, event)


@router.delete("/{event_id}")
async def delete_event(
        service: Annotated[EventService, Depends(event_service)],
        event_id: int,
        user: Annotated[UserReadSchema, Depends(current_user)],
):
    return await service.delete(event_id, user.id)
