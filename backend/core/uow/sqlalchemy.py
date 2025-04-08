from core.models import BetModel, EventModel, GameModel, MapModel, MatchModel, EATeamModel, TournamentModel, UserModel
from core.models.event import OutComeModel
from core.repository.bet import AbstractBetRepository, SQLAlchemyBetRepository
from core.repository.event import AbstractEventRepository, SQLAlchemyEventRepository, SQLAlchemyOutComeRepository
from core.repository.game import AbstractGameRepository, SQLAlchemyGameRepository
from core.repository.map import AbstractMapRepository, SQLAlchemyMapRepository
from core.repository.match import AbstractMatchRepository, SQLAlchemyMatchRepository
from core.repository.outcome import AbstractOutComeRepository
from core.repository.team import AbstractEATeamRepository, SQLAlchemyEATeamRepository
from core.repository.tournament import AbstractTournamentRepository, SQLAlchemyTournamentRepository
from core.repository.user import AbstractUserRepository, UserSQLAlchemyRepository
from .uow import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None

        self.bets: AbstractBetRepository | None
        self.events: AbstractEventRepository | None
        self.games: AbstractGameRepository | None
        self.maps: AbstractMapRepository | None
        self.matches: AbstractMatchRepository | None
        self.outcomes: AbstractOutComeRepository | None
        self.teams: AbstractEATeamRepository | None
        self.tournaments: AbstractTournamentRepository | None
        self.users: AbstractUserRepository | None

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
        return self

    async def __aexit__(self, exc_type, *_):
        if exc_type:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
