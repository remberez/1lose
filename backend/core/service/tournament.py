import typing

from .user import UserPermissionsService
from core.exceptions.common import NotFoundError
from core.uow.uow import UnitOfWork
from ..uow.utils import with_uow


class TournamentService:
    # TODO: Доработать логику по созданию/удалению/обновлению.
    def __init__(
        self,
        uow_factory: typing.Callable[[], UnitOfWork],
        permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def _is_exists(self, tournament_id: int, uow: UnitOfWork):
        if not await uow.tournaments.is_exists(tournament_id):
            raise NotFoundError(f"Tournament {tournament_id} not found")

    @with_uow
    async def create(self, user_id: int, uow: UnitOfWork, **tournament_data):
        tournament = await uow.tournaments.create(**tournament_data)
        return await uow.tournaments.get(tournament.id)

    @with_uow
    async def update(self, user_id: int, tournament_id: int, uow: UnitOfWork, **tournament_data):
        await self._is_exists(tournament_id, uow)
        tournament = await uow.tournaments.update(tournament_id, **tournament_data)
        return await uow.tournaments.get(tournament.id)

    @with_uow
    async def delete(self, user_id: int, tournament_id: int, uow: UnitOfWork):
        await self._is_exists(tournament_id, uow)
        return await uow.tournaments.delete(tournament_id)

    @with_uow
    async def list(self, uow: UnitOfWork):
        return await uow.tournaments.list()

    @with_uow
    async def get(self, tournament_id: int, uow: UnitOfWork):
        await self._is_exists(tournament_id, uow)
        return await uow.tournaments.get(tournament_id)
