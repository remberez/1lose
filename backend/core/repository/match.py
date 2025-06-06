from abc import ABC
from typing import Sequence

from sqlalchemy import select, and_, or_
from sqlalchemy.orm import joinedload, selectinload
from typing_extensions import TypeVar

from core.models import TournamentModel, EATeamModel, EventModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import (
    SQLAlchemyAbstractWriteRepository,
    SQLAlchemyAbstractReadRepository,
)
from core.models.match import MatchModel
import datetime

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
                    selectinload(EventModel.outcomes),
                    joinedload(EventModel.map),
                )
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self, is_live: bool = None, game_id: int = None) -> Sequence[MatchModel]:
        stmt = select(MatchModel).options(
            joinedload(MatchModel.first_team).joinedload(EATeamModel.game),
            joinedload(MatchModel.second_team).joinedload(EATeamModel.game),
            joinedload(MatchModel.tournament).joinedload(TournamentModel.game),
            joinedload(MatchModel.win_event).options(
                selectinload(EventModel.outcomes),
                joinedload(EventModel.map),
            )
        )

        if is_live is not None:
            filter_is_live = and_(MatchModel.date_end.is_(None), MatchModel.date_start <= datetime.datetime.now())
            filter_is_not_live = or_(MatchModel.date_end.is_not(None), MatchModel.date_start > datetime.datetime.now())
            
            stmt = stmt.where(
                filter_is_live if is_live else filter_is_not_live
            )

        if game_id is not None:
            stmt = stmt.where(
                MatchModel.first_team.has(EATeamModel.game_id == game_id) |
                MatchModel.second_team.has(EATeamModel.game_id == game_id) |
                MatchModel.tournament.has(TournamentModel.game_id == game_id)
            )
        
        result = await self._session.execute(stmt)
        return result.scalars().all()
