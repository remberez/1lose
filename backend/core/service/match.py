import typing
from datetime import datetime, timedelta, timezone

from core.exceptions.common import NotFoundError
from core.schema.match import MatchCreateSchema, MatchUpdateSchema

if typing.TYPE_CHECKING:
    from core.service.user import UserPermissionsService
    from core.repository.tournament import AbstractTournamentRepository
    from core.repository.match import AbstractMatchRepository
    from core.repository.team import AbstractEATeamRepository


class MatchService:
    def __init__(
            self,
            repository: "AbstractMatchRepository",
            tournament_repository: "AbstractTournamentRepository",
            permissions_service: "UserPermissionsService",
            team_repository: "AbstractEATeamRepository",
    ):
        self._repository = repository
        self._permissions_service = permissions_service
        self._tournament_repository = tournament_repository
        self._team_repository = team_repository

    async def is_exists(self, match_id: int):
        if not await self._repository.is_exists(match_id):
            raise NotFoundError(f"Match {match_id} not found")

    async def list(self):
        return await self._repository.list()

    async def get(self, match_id: int):
        await self.is_exists(match_id)
        return await self._repository.get(match_id)

    async def create(self, user_id: int, match_data: MatchCreateSchema):
        await self._permissions_service.verify_admin(user_id)

        current_time = datetime.now(timezone.utc)
        min_start_date = current_time + timedelta(hours=24)

        if match_data.date_start:
            if match_data.date_start.tzinfo is None:
                match_data.date_start = match_data.date_start.replace(tzinfo=timezone.utc)

            if match_data.date_start < min_start_date:
                raise ValueError("The start date must be at least 24 hours later than the current time")

        await self._tournament_repository.tournament_exists(match_data.tournament_id)

        return await self._repository.create(**match_data.model_dump())

    async def update(self, user_id: int, match_id: int, match_data: MatchUpdateSchema):
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(match_id)

        match = await self.get(match_id)
        if match_data.date_end and not match.date_start:
            raise ValueError("You can't end a match that's not in progress")

        return await self._repository.update(match_id, **match_data.model_dump(exclude_none=True))

    async def delete(self, user_id: int, match_id: int):
        await self._permissions_service.verify_admin(user_id)
        await self.is_exists(match_id)

        match = await self.get(match_id)
        match_is_on = match.date_start and match.date_start <= datetime.now() and not match.date_end
        if match_is_on:
            raise ValueError("You can't delete a match in progress")

        return await self._repository.delete(match_id)
