from core.config import settings
from core.schema.user import UserReadSchema
import datetime

from core.utils.auth import encode_token

TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"

def create_jwt(
        token_type: str,
        payload: dict,
        expire_minutes: int = settings.jwt_auth.access_token_lifetime_minutes,
        expire_timedelta: datetime.timedelta | None = None,
) -> str:
    jwt_payload = {"type": token_type}
    jwt_payload.update(payload)
    return encode_token(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(user: UserReadSchema) -> str:
    jwt_payload = {
        "sub": str(user.id),
        "email": user.email,
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        payload=jwt_payload,
        expire_minutes=settings.jwt_auth.access_token_lifetime_minutes,
    )


def create_refresh_token(user: UserReadSchema) -> str:
    jwt_payload = {
        "sub": str(user.id),
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        payload=jwt_payload,
        expire_timedelta=datetime.timedelta(days=settings.jwt_auth.refresh_token_lifetime_days)
    )
