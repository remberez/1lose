from fastapi_users.authentication import BearerTransport
from core.config import settings

# Определяет транспорт для токена.
bearer_transport = BearerTransport(tokenUrl=settings.api.token_url)
