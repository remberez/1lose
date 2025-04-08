from typing import Callable

from core.const.bet_status import BetStatus
from core.exceptions.user_exc import UserPermissionError
from core.schema.bet import BetCreateSchema, BetUpdateSchema
from core.service.user import UserPermissionsService
from core.exceptions.common import BusinessValidationError
from core.uow.uow import UnitOfWork


class BetService:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def list(self):
        # TODO: Использовать только для модераторов/администраторов
        ...

    async def user_list(self, user_id: int):
        async with self._uow_factory() as uow:
            return await uow.bets.user_bets(user_id)

    async def get(self, bet_id: int, user_id: int):
        # TODO:
        #   При добавлении тех. поддержки разрешить модераторам просматривать ставки,
        #   если активна сессия поддержки
        async with self._uow_factory() as uow:
            bet = await uow.bets.get(bet_id)

            if bet.user_id == user_id:
                return bet
            raise UserPermissionError()

    async def delete(self, bet_id: int, user_id: int):
        async with self._uow_factory() as uow:
            bet_owner_id = await uow.bets.bet_owner_id(bet_id)
            if bet_owner_id != user_id:
                await self._permissions_service.verify_admin(user_id)
            await uow.bets.delete(bet_id)

    async def create(self, user_id: int, bet: BetCreateSchema):
        async with self._uow_factory() as uow:
            user_balance = await uow.users.get_user_balance(user_id)

            if user_balance < bet.amount:
                raise BusinessValidationError("Insufficient funds on the balance sheet")

            outcome = await uow.outcomes.get(bet.outcome_id)
            event = await uow.events.get(bet.event_id)
            if outcome.id not in (event.first_outcome_id, event.second_outcome_id):
                raise BusinessValidationError("Outcome IDs do not match the event outcome IDs")

            await uow.users.update_user_balance(user_id, -bet.amount)

            return await uow.bets.create(
                **bet.model_dump(),
                user_id=user_id,
                coefficient=outcome.coefficient,
                bet_status=BetStatus.ACTIVE,
                possible_gain=bet.amount * outcome.coefficient,
            )

    async def update(self, bet_id: int, bet: BetUpdateSchema):
        ...

    async def sell(self, bet_id: int, user_id: int):
        # Продаёт ставку, устанавливает поле bet_status = 'sold' и возвращает часть денег на баланс пользователю
        ...
