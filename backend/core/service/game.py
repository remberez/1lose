from typing import Callable

from core.exceptions.common import NotFoundError
from core.schema.game import GameCreateSchema, GameReadSchema
from core.service.user import UserPermissionsService
from core.uow.uow import UnitOfWork


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

    async def create(self, game: GameCreateSchema, user_id: int) -> GameReadSchema:
        async with self._uow_factory() as uow:
            await self._permissions_service.verify_admin(user_id=user_id)
            return await uow.games.create(**game.model_dump())

    async def list(self) -> list[GameReadSchema]:
        async with self._uow_factory() as uow:
            return await uow.games.list()

    async def delete(self, game_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin(user_id)

        async with self._uow_factory() as uow:
            await self.is_exists(game_id)
            await uow.games.delete(game_id)

    async def get(self, game_id: int):
        await self.is_exists(game_id)

        async with self._uow_factory() as uow:
            return await uow.games.get(game_id)

    async def update(self, game_id: int, user_id: int, **game_data):
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(game_id)

        async with self._uow_factory() as uow:
            return await uow.games.update(game_id, **game_data)
