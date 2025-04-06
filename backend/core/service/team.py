from core.exceptions.common import NotFoundError
from core.repository.team import AbstractEATeamRepository
from core.repository.user import AbstractUserRepository
from core.service.user import UserPermissionsService


class EATeamService:
    def __init__(
        self,
        repository: AbstractEATeamRepository,
        user_repository: AbstractUserRepository,
        permissions_service: UserPermissionsService,
    ):
        self._repository = repository
        self._user_repository = user_repository
        self._permissions_service = permissions_service

    async def is_exists(self, team_id: int):
        if not await self._repository.is_exists(team_id):
            raise NotFoundError(f"Team {team_id} not found")

    async def list(self):
        return await self._repository.list()

    async def get(self, team_id: int):
        await self.is_exists(team_id)
        return await self._repository.get(team_id)

    async def create(self, user_id, **team_data):
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        team = await self._repository.create(**team_data)
        return await self._repository.get(team.id)

    async def delete(self, team_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)
        await self.is_exists(team_id)

        return await self._repository.delete(team_id)

    async def update(self, team_id: int, user_id: int, **team_data):
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)
        await self.is_exists(team_id)

        return await self._repository.update(team_id, **team_data)
