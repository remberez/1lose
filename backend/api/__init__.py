from fastapi import APIRouter
from core.config import settings
from .users import router as user_router
from .games import router as game_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(router=user_router)
router.include_router(router=game_router)
