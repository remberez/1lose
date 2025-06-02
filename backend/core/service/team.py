import os
import typing
import uuid

from typing_extensions import BinaryIO

from core.exceptions.common import NotFoundError
from core.schema.team import EATeamCreateSchema, EATeamUpdateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from core.utils.files import save_file


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

    @with_uow
    async def list(self, uow: UnitOfWork):
        return await uow.teams.list()

    @with_uow
    async def get(self, team_id: int, uow: UnitOfWork):
        await self._is_exists(team_id, uow=uow)
        return await uow.teams.get(team_id)

    @with_uow
    async def create(self, user_id, team: EATeamCreateSchema, icon: BinaryIO, uow: UnitOfWork):
        file_path = await save_file(icon, str(uuid.uuid4()) + ".png", "teams")
        team = await uow.teams.create(**team.model_dump(), icon_path=file_path)
        return await uow.teams.get(team.id)

    @with_uow
    async def delete(self, team_id: int, user_id: int, uow: UnitOfWork) -> None:
        await self._is_exists(team_id, uow=uow)
        team = await uow.teams.get(team_id)
        await uow.teams.delete(team_id)
        try:
            os.remove(team.icon_path)
        except FileNotFoundError:
            ...

    @with_uow
    async def update(
        self,
        team_id: int,
        user_id: int,
        team: EATeamUpdateSchema,
        icon: BinaryIO | None = None,
        uow: UnitOfWork = None
    ):
        await self._is_exists(team_id, uow=uow)

        if icon:
            team_model = await uow.teams.get(team_id)
            try:
                os.remove(team_model.icon_path)
            except FileNotFoundError:
                ...
            icon_path = await save_file(icon, str(uuid.uuid4()) + ".png", "teams")
            await uow.teams.update(team_id, **team.model_dump(exclude_none=True), icon_path=icon_path)
        else:
            await uow.teams.update(team_id, **team.model_dump(exclude_none=True))

        return await uow.teams.get(team_id)
