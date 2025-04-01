from typing import Optional

from fastapi_users import BaseUserManager, models, IntegerIDMixin
from starlette.requests import Request

from core.config import settings
from core.models import UserModel

import logging

from core.types.user_id import UserID

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[UserModel, UserID]):
    reset_password_token_secret = settings.auth.reset_password_token_secret
    verification_token_secret = settings.auth.verification_token_secret

    async def on_after_forgot_password(
        self, user: models.UP, token: str, request: Optional[Request] = None
    ) -> None:
        log.warning("User %r has forgot password. Reset token: %r", user.id, token)

    async def on_after_register(
        self, user: models.UP, request: Optional[Request] = None
    ) -> None:
        log.warning("User %r has registered.", user.id)

    async def on_after_request_verify(
        self, user: models.UP, token: str, request: Optional[Request] = None
    ) -> None:
        log.warning(
            "Verification requested for user %r. Verification token: %r", user.id, token
        )
