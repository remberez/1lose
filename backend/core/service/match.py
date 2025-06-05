import typing
from datetime import datetime, timedelta, timezone

from core.exceptions.common import NotFoundError
from core.exceptions.match_exc import MatchInProgressException, MatchDateTimeException
from core.schema.match import MatchCreateSchema, MatchUpdateSchema, MathFilterSchema
from core.uow.uow import UnitOfWork
from core.uow.utils import with_uow

if typing.TYPE_CHECKING:
    from core.service.user import UserPermissionsService


class MatchService:
    def __init__(
        self,
        uow_factory: typing.Callable[[], UnitOfWork],
        permissions_service: "UserPermissionsService"
    ):
        self._permissions_service = permissions_service
        self._uow_factory = uow_factory

    async def _match_data_exists(
        self,
        first_team_id: int | None,
        second_team_id: int | None,
        tournament_id: int | None,
        uow: UnitOfWork,
    ):
        msgs = []
        if first_team_id and not await uow.teams.is_exists(first_team_id):
            msgs.append(f"Team {first_team_id} not found")
        if second_team_id and not await uow.teams.is_exists(second_team_id):
            msgs.append(f"Team {second_team_id} not found")
        if tournament_id and not await uow.tournaments.is_exists(tournament_id):
            msgs.append(f"Tournament {tournament_id} not found")

        if msgs:
            raise NotFoundError(*msgs)

    async def _is_exists(self, match_id: int, uow: UnitOfWork):
        if not await uow.matches.is_exists(match_id):
            raise NotFoundError(f"Match {match_id} not found")

    @with_uow
    async def list(self, filters: MathFilterSchema, uow: UnitOfWork):
        return await uow.matches.list(is_live=filters.is_live, game_id=filters.game_id)

    @with_uow
    async def get(self, match_id: int, uow: UnitOfWork):
        await self._is_exists(match_id, uow)
        return await uow.matches.get(match_id)

    @with_uow
    async def create(self, user_id: int, match_data: MatchCreateSchema, uow: UnitOfWork):
        current_time = datetime.now(timezone.utc)
        min_start_date = current_time + timedelta(hours=24)

        if match_data.date_start:
            if match_data.date_start.tzinfo is None:
                match_data.date_start = match_data.date_start.replace(tzinfo=timezone.utc)
            if match_data.date_start < min_start_date:
                raise MatchDateTimeException("The start date must be at least 24 hours later than the current time")

        await self._match_data_exists(
            first_team_id=match_data.first_team_id,
            second_team_id=match_data.second_team_id,
            tournament_id=match_data.tournament_id,
            uow=uow,
        )

        match = await uow.matches.create(**match_data.model_dump(), score=[0, 0])
        return await uow.matches.get(match.id)

    @with_uow
    async def update(self, user_id: int, match_id: int, match_data: MatchUpdateSchema, uow: UnitOfWork):
        await self._is_exists(match_id, uow)

        match = await self.get(match_id)
        if match_data.date_end and not match.date_start:
            raise MatchInProgressException("You can't end a match that's not in progress")

        match = await uow.matches.update(
            match_id, **match_data.model_dump(exclude_none=True)
        )
        return await uow.matches.get(match.id)

    @with_uow
    async def delete(self, user_id: int, match_id: int, uow: UnitOfWork):
        await self._is_exists(match_id, uow)

        match = await self.get(match_id)
        match_is_on = (
            match.date_start
            and match.date_start <= datetime.now(timezone.utc)
            and not match.date_end
        )
        if match_is_on:
            raise MatchInProgressException("You can't delete a match in progress")

        return await uow.matches.delete(match_id)
