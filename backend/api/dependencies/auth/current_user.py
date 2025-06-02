from typing import Annotated

from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from core.config import settings
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

async def get_current_user_from_token_type(token_type: str):
    ...


async def get_current_active_verify_user(

):
    ...


async def get_current_user(

):
    ...


async def get_active_user(

):
    ...


async def get_verified_user(

):
    ...
