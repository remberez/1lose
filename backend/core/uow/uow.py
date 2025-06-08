from abc import abstractmethod, ABC
from typing import Self

from core.repository.bet import AbstractBetRepository
from core.repository.business_settings import AbstractBusinessSettingsRepository
from core.repository.event import AbstractEventRepository
from core.repository.event_outcome import AbstractEventOutcomeRepository
from core.repository.event_type import AbstractEventTypeRepository
from core.repository.game import AbstractGameRepository
from core.repository.map import AbstractMapRepository
from core.repository.match import AbstractMatchRepository
from core.repository.outcome import AbstractOutComeRepository
from core.repository.team import AbstractEATeamRepository
from core.repository.tournament import AbstractTournamentRepository
from core.repository.user import AbstractUserRepository


class UnitOfWork(ABC):
    bets: AbstractBetRepository | None
    events: AbstractEventRepository | None
    games: AbstractGameRepository | None
    maps: AbstractMapRepository | None
    matches: AbstractMatchRepository | None
    outcomes: AbstractOutComeRepository | None
    teams: AbstractEATeamRepository | None
    tournaments: AbstractTournamentRepository | None
    users: AbstractUserRepository | None
    business_settings: AbstractBusinessSettingsRepository | None
    event_outcome: AbstractEventOutcomeRepository | None
    event_type: AbstractEventTypeRepository | None = None

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self) -> Self:
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...
