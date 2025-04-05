from datetime import datetime, timedelta

from core.repository.match import AbstractMatchRepository
from core.schema.match import MatchCreateSchema, MatchUpdateSchema
from core.service.user import UserPermissionsService


class MatchService:
    def __init__(
            self,
            repository: AbstractMatchRepository,
            permissions_service: UserPermissionsService,
    ):
        self._repository = repository
        self._permissions_service = permissions_service

    async def list(self):
        return await self._repository.list()

    async def get(self, match_id: int):
        return await self._repository.get(match_id)

    async def create(self, user_id: int, match_data: MatchCreateSchema):
        await self._permissions_service.verify_admin(user_id)

        min_start_date = datetime.now() + timedelta(hours=24)
        if match_data.date_start and match_data.date_start < min_start_date:
            raise ValueError("The start date must be at least 24 hours later than the current time")

        return await self._repository.create(**match_data.model_dump())

    async def update(self, user_id: int, match_id: int, match_data: MatchUpdateSchema):
        await self._permissions_service.verify_admin(user_id)

        match = await self.get(match_id)
        if match_data.date_end and not match.date_start:
            raise ValueError("You can't end a match that's not in progress")

        return await self._repository.update(match_id, **match_data.model_dump(exclude_none=True))

    async def delete(self, user_id: int, match_id: int):
        await self._permissions_service.verify_admin(user_id)

        match = await self.get(match_id)
        match_is_on = match.date_start and match.date_start <= datetime.now() and not match.date_end
        if match_is_on:
            raise ValueError("You can't delete a match in progress")

        return await self._repository.delete(match_id)
