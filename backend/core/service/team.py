import typing

from core.exceptions.common import NotFoundError
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork


class EATeamService:
    def __init__(
            self,
            uow_factory: typing.Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def _is_exists(self, team_id: int, uow: UnitOfWork):
        if not await uow.teams.is_exists(team_id):
            raise NotFoundError(f"Team {team_id} not found")

    async def list(self):
        async with self._uow_factory() as uow:
            return await uow.teams.list()

    async def get(self, team_id: int):
        async with self._uow_factory() as uow:
            await self._is_exists(team_id, uow=uow)
            return await uow.teams.get(team_id)

    async def create(self, user_id, **team_data):
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        async with self._uow_factory() as uow:
            team = await uow.teams.create(**team_data)
            return await uow.teams.get(team.id)

    async def delete(self, team_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        async with self._uow_factory() as uow:
            await self._is_exists(team_id, uow=uow)
            return await uow.teams.delete(team_id)

    async def update(self, team_id: int, user_id: int, **team_data):
        await self._permissions_service.verify_admin_or_moderator(user_id=user_id)

        async with self._uow_factory() as uow:
            await self._is_exists(team_id, uow=uow)
            return await uow.teams.update(team_id, **team_data)
