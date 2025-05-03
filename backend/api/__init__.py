from fastapi import APIRouter
from core.config import settings
from .auth import router as auth_router
from .games import router as game_router
from .teams import router as team_router
from .tournament import router as tournament_router
from .match import router as match_router
from .map import router as map_router
from .event import router as event_router
from .bet import router as bet_router
from .business_settings import router as business_settings_router
from .users import router as user_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(router=user_router)
router.include_router(router=game_router)
router.include_router(router=team_router)
router.include_router(router=tournament_router)
router.include_router(router=match_router)
router.include_router(router=map_router)
router.include_router(router=event_router)
router.include_router(router=bet_router)
router.include_router(router=business_settings_router)
router.include_router(router=auth_router)
