from fastapi_users.authentication import AuthenticationBackend

from api.dependencies.auth.stategy import get_database_strategy
from core.auth.transport import bearer_transport

auth_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
