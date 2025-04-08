from core.exceptions.user_exc import UserPermissionError
from core.repository.bet import AbstractBetRepository
from core.repository.user import AbstractUserRepository
from core.schema.bet import BetCreateSchema, BetUpdateSchema
from core.service.user import UserPermissionsService
from core.exceptions.common import BusinessValidationError


class BetService:
    def __init__(
            self,
            repo: AbstractBetRepository,
            permissions_service: UserPermissionsService,
            user_repository: AbstractUserRepository,
    ):
        self._repo = repo
        self._permissions_service = permissions_service
        self._user_repo = user_repository

    async def list(self):
        # TODO: Использовать только для модераторов/администраторов
        ...

    async def user_list(self, user_id: int):
        return await self._repo.user_bets(user_id)

    async def get(self, bet_id: int, user_id: int):
        # TODO:
        #   При добавлении тех. поддержки разрешить модераторам просматривать ставки,
        #   если активна сессия поддержки
        bet = await self._repo.get(bet_id)

        if bet.user_id == user_id or (await self._permissions_service.verify_admin_or_moderator(user_id)):
            return bet
        raise UserPermissionError()

    async def delete(self, bet_id: int, user_id: int):
        ...

    async def create(self, user_id: int, bet: BetCreateSchema):
        user_balance = await self._user_repo.get_user_balance(user_id)

        if user_balance < bet.amount:
            raise BusinessValidationError("Insufficient funds on the balance sheet")

        await self._user_repo.update_user_balance(user_id, -bet.amount)
        return await self._repo.create(**bet.model_dump(), user_id=user_id)

    async def update(self, bet_id: int, bet: BetUpdateSchema):
        ...

    async def sell(self, bet_id: int, user_id: int):
        # Продаёт ставку, устанавливает поле bet_status = 'sold' и возвращает часть денег на баланс пользователю
        ...
