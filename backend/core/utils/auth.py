import datetime

import bcrypt
import jwt

from core.config import settings


def encode_token(
        payload: dict,
        private_key: str = settings.jwt_auth.private_key,
        algorithm: str = settings.jwt_auth.algorithm,
        expire_minutes: int = settings.jwt_auth.access_token_lifetime_minutes,
        expire_timedelta: datetime.timedelta | None = None,
) -> str:
    now = datetime.datetime.now(datetime.UTC)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + datetime.timedelta(minutes=expire_minutes)

    to_encoded = payload.copy()
    to_encoded.update(
        exp=expire,
        iat=now,
    )

    encoded = jwt.encode(
        to_encoded,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_token(
        token: str | bytes,
        public_key: str = settings.jwt_auth.public_key,
        algorithm: str = settings.jwt_auth.algorithm,
):
    payload = jwt.decode(token, public_key, algorithms=[algorithm])
    return payload


def hash_password(
        password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes,
):
    return bcrypt.checkpw(password.encode(), hashed_password)
