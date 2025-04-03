from core.const.user_role import UserRoleCodes
from core.exceptions.user_exc import UserPermissionError
from core.repository.team import AbstractEATeamRepository
from core.repository.user import AbstractUserRepository

class EATeamService:
    def __init__(
            self,
            repository: AbstractEATeamRepository,
            user_repository: AbstractUserRepository,
    ):
        self._repository = repository
        self._user_repository = user_repository

    async def list(self):
        return self._repository.list()

    async def get(self, team_id: int):
        return self.get(team_id)

    async def create(self, user_id, **team_data):
        user = await self._user_repository.get(user_id)

        if user.role_code in (UserRoleCodes.ADMIN.value, UserRoleCodes.MODERATOR.value):
            return await self._repository.create(**team_data)
        else:
            raise UserPermissionError()
