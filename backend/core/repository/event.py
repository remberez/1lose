from abc import ABC
from typing import Sequence

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

    async def _create_outcome(self, **outcome_data) -> int:
        stmt = (
            insert(OutComeModel)
            .values(**outcome_data)
            .returning(OutComeModel.id)
        )
        result = await self._session.execute(stmt)
        outcome_id = result.scalar_one()
        await self._session.commit()
        return outcome_id

    async def create(self, **model_data) -> EventModel:
        first_outcome, second_outcome = model_data.pop("first_outcome"), model_data.pop("second_outcome")

        if not (first_outcome and second_outcome):
            raise ValueError("Required fields 'first_outcome' and 'second_outcome'")

        model_data["first_outcome_id"] = await self._create_outcome(**first_outcome)
        model_data["second_outcome_id"] = await self._create_outcome(**second_outcome)

        stmt = (
            insert(EventModel)
            .values(**model_data)
            .returning(EventModel.id)
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        return await self.get(result.scalar())
