from abc import ABC
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing_extensions import TypeVar

from core.models import TournamentModel, EATeamModel, EventModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import (
    SQLAlchemyAbstractWriteRepository,
    SQLAlchemyAbstractReadRepository,
)
from core.models.match import MatchModel

MatchT = TypeVar("MatchT")


class AbstractMatchRepository(
    AbstractReadRepository[MatchT],
    AbstractWriteRepository[MatchT],
    ABC,
):
    # Специфичные методы для работы с MatchModel
    ...


class SQLAlchemyMatchRepository(
    SQLAlchemyAbstractWriteRepository[MatchModel],
    SQLAlchemyAbstractReadRepository[MatchModel],
    AbstractMatchRepository,
):
    async def get(self, model_id: int) -> MatchModel | None:
        stmt = (
            select(MatchModel)
            .where(MatchModel.id == model_id)
            .options(
                joinedload(MatchModel.first_team).joinedload(EATeamModel.game),
                joinedload(MatchModel.second_team).joinedload(EATeamModel.game),
                joinedload(MatchModel.tournament).joinedload(TournamentModel.game),
                joinedload(MatchModel.win_event).options(
                    joinedload(EventModel.first_outcome),
                    joinedload(EventModel.second_outcome),
                    joinedload(EventModel.map),
            )
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self, is_live: bool = None) -> Sequence[MatchModel]:
        stmt = select(MatchModel).options(
            joinedload(MatchModel.first_team).joinedload(EATeamModel.game),
            joinedload(MatchModel.second_team).joinedload(EATeamModel.game),
            joinedload(MatchModel.tournament).joinedload(TournamentModel.game),
            joinedload(MatchModel.win_event).options(
                joinedload(EventModel.first_outcome),
                joinedload(EventModel.second_outcome),
                joinedload(EventModel.map),
            )
        )

        if is_live is not None:
            stmt = stmt.where(
                MatchModel.date_end.is_(None) if is_live
                else MatchModel.date_end.is_not(None)
            )

        result = await self._session.execute(stmt)
        return result.scalars().all()
