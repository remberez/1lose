from fastapi_users import FastAPIUsers

from api.dependencies.auth.backend import auth_backend
from api.dependencies.auth.user_manager import get_user_manager
from core.models import UserModel
from core.types.user_id import UserID

fastapi_users = FastAPIUsers[UserModel, UserID](
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend],
)
