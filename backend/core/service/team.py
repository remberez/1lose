from core.const.user_role import UserRoleCodes
from core.exceptions.user_exc import UserPermissionError
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

    async def list(self):
        return await self._repository.list()

    async def get(self, team_id: int):
        return await self._repository.get(team_id)

    async def create(self, user_id, **team_data):
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        team = await self._repository.create(**team_data)
        return await self._repository.get(team.id)

    async def delete(self, team_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        return await self._repository.delete(team_id)
