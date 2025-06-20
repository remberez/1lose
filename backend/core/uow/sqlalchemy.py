from core.models import (
    BetModel, EventModel, GameModel,
    MapModel, MatchModel, EATeamModel,
    TournamentModel, UserModel, BusinessSettings,
)
from core.models.event import OutComeModel, EventOutcomeModel, EventTypeModel
from core.repository.bet import AbstractBetRepository, SQLAlchemyBetRepository
from core.repository.event import AbstractEventRepository, SQLAlchemyEventRepository
from core.repository.game import AbstractGameRepository, SQLAlchemyGameRepository
from core.repository.map import AbstractMapRepository, SQLAlchemyMapRepository
from core.repository.match import AbstractMatchRepository, SQLAlchemyMatchRepository
from core.repository.outcome import AbstractOutComeRepository, SQLAlchemyOutComeRepository
from core.repository.team import AbstractEATeamRepository, SQLAlchemyEATeamRepository
from core.repository.tournament import AbstractTournamentRepository, SQLAlchemyTournamentRepository
from core.repository.user import AbstractUserRepository, UserSQLAlchemyRepository
from .uow import UnitOfWork
from ..repository.business_settings import SQLAlchemyBusinessSettingsRepository
from ..repository.event_outcome import AbstractEventOutcomeRepository, SQLAlchemyEventOutcomeRepository
from ..repository.event_type import SQLAlchemyEventTypeRepository, AbstractEventTypeRepository


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None

        self.bets: AbstractBetRepository | None = None
        self.events: AbstractEventRepository | None = None
        self.games: AbstractGameRepository | None = None
        self.maps: AbstractMapRepository | None = None
        self.matches: AbstractMatchRepository | None = None
        self.outcomes: AbstractOutComeRepository | None = None
        self.teams: AbstractEATeamRepository | None = None
        self.tournaments: AbstractTournamentRepository | None = None
        self.users: AbstractUserRepository | None = None
        self.event_outcome: AbstractEventOutcomeRepository | None = None
        self.event_type: AbstractEventTypeRepository | None = None

    async def __aenter__(self):
        self.session = self.session_factory()

        self.bets = SQLAlchemyBetRepository(session=self.session, model=BetModel)
        self.events = SQLAlchemyEventRepository(session=self.session, model=EventModel)
        self.games = SQLAlchemyGameRepository(session=self.session, model=GameModel)
        self.maps = SQLAlchemyMapRepository(session=self.session, model=MapModel)
        self.matches = SQLAlchemyMatchRepository(session=self.session, model=MatchModel)
        self.outcomes = SQLAlchemyOutComeRepository(session=self.session, model=OutComeModel)
        self.teams = SQLAlchemyEATeamRepository(session=self.session, model=EATeamModel)
        self.tournaments = SQLAlchemyTournamentRepository(session=self.session, model=TournamentModel)
        self.users = UserSQLAlchemyRepository(session=self.session, model=UserModel)
        self.business_settings = SQLAlchemyBusinessSettingsRepository(session=self.session, model=BusinessSettings)
        self.event_outcome = SQLAlchemyEventOutcomeRepository(session=self.session, model=EventOutcomeModel)
        self.event_type = SQLAlchemyEventTypeRepository(session=self.session, model=EventTypeModel)

        return self

    async def __aexit__(self, exc_type, *_):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
