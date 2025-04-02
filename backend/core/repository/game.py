from .sqlalchemy import SQLAlchemyAbstractRepository
from core.models.game import GameModel


class GameRepository(SQLAlchemyAbstractRepository[GameModel]):
    async def list(self, *args, **kwargs) -> list[GameModel]:
        ...

    async def get(self, **kwargs) -> GameModel:
        ...

    async def delete(self, model_id: int) -> None:
        ...

    async def update(self, model_id: int, **data) -> GameModel:
        ...

    async def create(self, **data) -> GameModel:
        ...
