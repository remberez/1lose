from core.repository.tournament import AbstractTournamentRepository
from .user import UserPermissionsService
from ..exceptions.common import NotFoundError


class TournamentService:
    # TODO: Доработать логику по созданию/удалению/обновлению.
    def __init__(
            self,
            repository: AbstractTournamentRepository,
            permissions_service: UserPermissionsService,
    ):
        self._repository = repository
        self._permissions_service = permissions_service

    async def is_exists(self, tournament_id: int):
        if not await self._repository.is_exists(tournament_id):
            raise NotFoundError(f"Tournament {tournament_id} not found")

    async def create(self, user_id: int, **tournament_data):
        await self._permissions_service.verify_admin_or_moderator(user_id)
        return await self._repository.create(**tournament_data)

    async def update(self, user_id: int, tournament_id: int, **tournament_data):
        await self._permissions_service.verify_admin_or_moderator(user_id)
        await self.is_exists(tournament_id)
        return await self._repository.update(tournament_id, **tournament_data)

    async def delete(self, user_id: int, tournament_id: int):
        await self._permissions_service.verify_admin_or_moderator(user_id)
        await self.is_exists(tournament_id)
        return await self._repository.delete(tournament_id)

    async def list(self):
        return await self._repository.list()

    async def get(self, tournament_id):
        await self.is_exists(tournament_id)
        return await self._repository.get(tournament_id)
