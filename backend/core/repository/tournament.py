from abc import ABC
from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload
from typing_extensions import TypeVar

from core.models import TournamentModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractRepository

TournamentT = TypeVar("TournamentT")


class AbstractTournamentRepository(
    AbstractReadRepository,
    AbstractWriteRepository,
    ABC,
):
    # Специфичные методы для работы с TournamentModel
    ...


class SQLAlchemyTournamentRepository(
    SQLAlchemyAbstractRepository[TournamentModel],
    AbstractTournamentRepository,
):
    async def list(self) -> Sequence[TournamentModel]:
        stmt = select(TournamentModel)
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
