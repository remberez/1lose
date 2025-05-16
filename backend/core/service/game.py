import logging
import os
import uuid
from typing import Callable, BinaryIO

from core.exceptions.common import NotFoundError
from core.schema.game import GameCreateSchema, GameReadSchema, GameUpdateSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork
from core.utils.files import save_file

log = logging.getLogger(__name__)


class GameService:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            permissions_service: UserPermissionsService
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def is_exists(self, game_id: int):
        async with self._uow_factory() as uow:
            if not await uow.games.is_exists(game_id):
                raise NotFoundError(f"Game {game_id} not found")

    async def create(self, game: GameCreateSchema, icon: BinaryIO, user_id: int) -> GameReadSchema:
        async with self._uow_factory() as uow:
            await self._permissions_service.verify_admin(user_id=user_id)
            icon_path = await save_file(icon, str(uuid.uuid4()) + ".png", "/games")
            return await uow.games.create(**game.model_dump(), icon_path=icon_path)

    async def list(self) -> list[GameReadSchema]:
        async with self._uow_factory() as uow:
            return await uow.games.list()

    async def delete(self, game_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin(user_id)

        async with self._uow_factory() as uow:
            await self.is_exists(game_id)
            game = await uow.games.get(game_id)
            try:
                os.remove(game.icon_path)
            except FileNotFoundError:
                log.warning(f"Файл {game.icon_path} не был найден. Удаление без поиска файла.")
            await uow.games.delete(game_id)

    async def get(self, game_id: int):
        await self.is_exists(game_id)

        async with self._uow_factory() as uow:
            return await uow.games.get(game_id)

    async def update(self, game_id: int, user_id: int, game: GameUpdateSchema, icon: BinaryIO | None = None):
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(game_id)

        async with self._uow_factory() as uow:
            if icon:
                game_model = await uow.games.get(game_id)
                try:
                    os.remove(game_model.icon_path)
                except FileNotFoundError:
                    ...

                icon_path = await save_file(icon, str(uuid.uuid4()) + ".png", "games")
                return await uow.games.update(game_id, **game.model_dump(exclude_none=True), icon_path=icon_path)
            else:
                return await uow.games.update(game_id, **game.model_dump(exclude_none=True))
