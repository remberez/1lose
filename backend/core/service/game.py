from core.repository.game import GameRepository
from core.schema.game import GameCreateSchema, GameReadSchema


class GameService:
    def __init__(self, repository: GameRepository):
        self._repository = repository

    async def create(self, game: GameCreateSchema) -> GameReadSchema:
        return await self._repository.create(**game.model_dump())
