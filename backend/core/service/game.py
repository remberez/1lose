from core.const.user_role import UserRoleCodes
from core.exceptions.user_exc import UserPermissionError
from core.repository.game import AbstractGameRepository
from core.repository.user import AbstractUserRepository
from core.schema.game import GameCreateSchema, GameReadSchema


class GameService:
    def __init__(self, repository: AbstractGameRepository, user_repository: AbstractUserRepository):
        self._repository = repository
        self._user_repository = user_repository

    async def create(self, game: GameCreateSchema, user_id: int) -> GameReadSchema:
        user = await self._user_repository.get(user_id)

        if user.role_code == UserRoleCodes.ADMIN.value:
            return await self._repository.create(**game.model_dump())
        raise UserPermissionError()

    async def list(self) -> list[GameReadSchema]:
        return await self._repository.list()
