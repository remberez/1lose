from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from core.config import settings
from core.schema.bet import BetCreateSchema, BetReadSchema
from core.schema.user import UserReadSchema
from core.service.bet import BetService
from .dependencies.auth.current_user import current_user
from .dependencies.services.bet import bet_service

router = APIRouter(prefix=settings.api.bet, tags=["Bets"])


@router.post("/", response_model=BetReadSchema)
async def create_bet(
        user: Annotated[UserReadSchema, Depends(current_user)],
        bet: BetCreateSchema,
        service: Annotated[BetService, Depends(bet_service)],
):
    return await service.create(user_id=user.id, bet=bet)
