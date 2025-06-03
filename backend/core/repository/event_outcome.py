from typing import Any

from core.models.event import EventOutcomeModel, EventModel
from core.repository.sqlalchemy import SQLAlchemyAbstractRepository


class AbstractEventOutcomeRepository:
    async def create_relationship(self, event_id: int, outcome_id: int) -> Any:
        raise NotImplementedError()


class SQLAlchemyEventOutcomeRepository(
    AbstractEventOutcomeRepository,
    SQLAlchemyAbstractRepository,
):
    async def create_relationship(self, event_id: int, outcome_id: int) -> EventOutcomeModel:
        model = EventOutcomeModel(event_id=event_id, outcome_id=outcome_id)
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(await self._session.get(EventModel, event_id))
        return model
