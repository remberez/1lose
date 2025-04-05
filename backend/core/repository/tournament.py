from abc import ABC
from typing import Sequence

from sqlalchemy import select, update, delete, exists
from sqlalchemy.orm import joinedload
from typing_extensions import TypeVar

from core.exceptions.common import NotFoundError
from core.models import TournamentModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractRepository

TournamentT = TypeVar("TournamentT")


class AbstractTournamentRepository(
    AbstractReadRepository[TournamentT],
    AbstractWriteRepository[TournamentT],
    ABC,
):
    # Специфичные методы для работы с TournamentModel
    async def tournament_exists(self, tournament_id: int) -> bool:
        raise NotImplementedError()


class SQLAlchemyTournamentRepository(
    SQLAlchemyAbstractRepository[TournamentModel],
    AbstractTournamentRepository,
):
    async def list(self) -> Sequence[TournamentModel]:
        stmt = (
            select(TournamentModel)
            .options(
                joinedload(TournamentModel.game)
            )
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get(self, tournament_id: int) -> TournamentModel | None:
        stmt = (
            select(TournamentModel)
            .where(TournamentModel.id == tournament_id)
            .options(joinedload(TournamentModel.game))
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, **data) -> TournamentModel | None:
        tournament = TournamentModel(**data)
        self._session.add(tournament)
        await self._session.commit()
        await self._session.refresh(tournament)

        loaded_tournament = await self.get(tournament.id)
        return loaded_tournament

    async def update(self, tournament_id: int, **data) -> TournamentModel:
        stmt = (
            update(TournamentModel)
            .where(TournamentModel.id == tournament_id)
            .values(**data)
        )
        await self._session.execute(stmt)
        await self._session.commit()

        tournament = await self.get(tournament_id)
        return tournament

    async def delete(self, tournament_id: int) -> None:
        stmt = (
            delete(TournamentModel)
            .where(TournamentModel.id == tournament_id)
        )
        await self._session.execute(stmt)
        await self._session.commit()

    async def tournament_exists(self, tournament_id: int) -> None:
        # Вызывает NotFoundError, если турнир не был найден.
        stmt = select(exists().where(TournamentModel.id == tournament_id))
        if not bool(await self._session.scalar(stmt)):
            raise NotFoundError(f"Tournament {tournament_id} not found")
