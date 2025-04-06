from core.exceptions.common import NotFoundError
from core.repository.game import AbstractGameRepository
from core.repository.user import AbstractUserRepository
from core.schema.game import GameCreateSchema, GameReadSchema
from core.service.user import UserPermissionsService


class GameService:
    def __init__(
        self,
        repository: AbstractGameRepository,
        user_repository: AbstractUserRepository,
        permissions_service: UserPermissionsService,
    ):
        self._repository = repository
        self._user_repository = user_repository
        self._permissions_service = permissions_service

    async def is_exists(self, game_id: int):
        if not await self._repository.is_exists(game_id):
            raise NotFoundError(f"Game {game_id} not found")

    async def create(self, game: GameCreateSchema, user_id: int) -> GameReadSchema:
        await self._permissions_service.verify_admin(user_id=user_id)
        return await self._repository.create(**game.model_dump())

    async def list(self) -> list[GameReadSchema]:
        return await self._repository.list()

    async def delete(self, game_id: int, user_id: int) -> None:
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(game_id)
        await self._repository.delete(game_id)

    async def get(self, game_id: int):
        await self.is_exists(game_id)
        return await self._repository.get(game_id)

    async def update(self, game_id: int, user_id: int, **game_data):
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(game_id)
        return await self._repository.update(game_id, **game_data)
