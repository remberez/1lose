from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from core.auth.jwt import TOKEN_TYPE_FIELD, ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE
from api.dependencies.services.user import get_user_service
from core.config import settings
from core.exceptions.user_exc import UserPermissionError
from core.schema.user import UserReadSchema
from core.service.user import UserService
from core.utils.auth import decode_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl=settings.api.token_url)

async def get_current_token_payload(
    token: Annotated[str, Depends(oauth2_schema)],
) -> dict:
    # Принимает в себя токен в запросе и возвращает payload токена
    invalid_token_exc = HTTPException(
        status_code=401,
        detail="Token invalid"
    )
    try:
        payload = decode_token(token)
    except InvalidTokenError:
        raise invalid_token_exc
    return payload


def validate_token_type(
        payload: dict,
        token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if token_type != current_token_type:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid token type {current_token_type!r} expected {token_type!r}"
        )
    return True


def get_current_user_from_token_of_type(token_type: str):
    async def get_user_from_token(
            payload: Annotated[dict, Depends(get_current_token_payload)],
            user_service: Annotated[UserService, Depends(get_user_service)]
    ) -> UserReadSchema:
        validate_token_type(payload, token_type)
        user_id = payload.get("sub")
        if user := await user_service.get(int(user_id)):
            return user
        raise HTTPException(
            status_code=401,
            detail="Invalid token (not found)",
        )
    return get_user_from_token


get_current_user = get_current_user_from_token_of_type(ACCESS_TOKEN_TYPE)
get_current_user_refresh = get_current_user_from_token_of_type(REFRESH_TOKEN_TYPE)

CurrentUser = Annotated[UserReadSchema, Depends(get_current_user)]
CurrentUserRefresh = Annotated[UserReadSchema, Depends(get_current_user_refresh)]


async def get_current_active_verify_user(
        user: CurrentUser
):
    if not user.is_active or not user.is_verified:
        raise UserPermissionError("Account is inactive or unverified")
    return user


async def get_active_user(
        user: CurrentUser
):
    if not user.is_active:
        raise UserPermissionError("Account is inactive")
    return user


async def get_verified_user(
        user: CurrentUser
):
    if not user.is_verified:
        raise UserPermissionError("Account is verified")
    return user


CurrentVerifiedActiveUser = Annotated[UserReadSchema, get_current_active_verify_user]
CurrentActiveUser = Annotated[UserReadSchema, get_active_user]
CurrentVerifiedUser = Annotated[UserReadSchema, get_verified_user]
