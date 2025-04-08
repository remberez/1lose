from abc import ABC, abstractmethod
from typing import Sequence, cast

from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from core.models import EventModel, MatchModel, MapModel, TournamentModel, EATeamModel
from core.models.event import OutComeModel
from core.repository.abc import AbstractReadRepository, AbstractWriteRepository
from core.repository.sqlalchemy import SQLAlchemyAbstractReadRepository, SQLAlchemyAbstractWriteRepository


class AbstractEventRepository[Model](
    AbstractReadRepository[Model],
    AbstractWriteRepository[Model],
    ABC,
):
    # Специфичные методы для работы с EventModel
    @abstractmethod
    async def get_outcomes(self, event_id: int) -> Sequence:
        raise NotImplementedError()


class AbstractOutComeRepository[Model](
    AbstractReadRepository[Model],
    ABC,
):
    # Специфичные методы для работы с OutComeModel
    ...


class SQLAlchemyEventRepository(
    AbstractEventRepository[EventModel],
    SQLAlchemyAbstractReadRepository[EventModel],
    SQLAlchemyAbstractWriteRepository[EventModel],
):
    async def get(self, event_id: int) -> EventModel | None:
        stmt = (
            select(EventModel)
            .where(EventModel.id == event_id)
            .options(
                joinedload(EventModel.match).joinedload(MatchModel.tournament).joinedload(TournamentModel.game),
                joinedload(EventModel.match).joinedload(MatchModel.first_team).joinedload(EATeamModel.game),
                joinedload(EventModel.match).joinedload(MatchModel.second_team).joinedload(EATeamModel.game),
                joinedload(EventModel.map).joinedload(MapModel.match),
                joinedload(EventModel.first_outcome),
                joinedload(EventModel.second_outcome),
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self, *args, **kwargs) -> Sequence[EventModel]:
        stmt = (
            select(EventModel)
            .options(
                joinedload(EventModel.match).joinedload(MatchModel.tournament).joinedload(TournamentModel.game),
                joinedload(EventModel.match).joinedload(MatchModel.first_team).joinedload(EATeamModel.game),
                joinedload(EventModel.match).joinedload(MatchModel.second_team).joinedload(EATeamModel.game),
                joinedload(EventModel.map).joinedload(MapModel.match),
                joinedload(EventModel.first_outcome),
                joinedload(EventModel.second_outcome),
            )
        )
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def create(self, **model_data) -> EventModel:
        stmt = (
            insert(EventModel)
            .values(**model_data)
            .returning(EventModel.id)
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        return await self.get(result.scalar())

    async def get_outcomes(self, event_id: int) -> tuple[OutComeModel, OutComeModel]:
        event = await self._session.get(EventModel, event_id)
        return cast(OutComeModel, event.first_outcome), cast(OutComeModel, event.second_outcome)


class SQLAlchemyOutComeRepository(
    AbstractOutComeRepository[OutComeModel],
    SQLAlchemyAbstractReadRepository[OutComeModel],
):
    ...
