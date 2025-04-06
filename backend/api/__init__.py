from fastapi import APIRouter
from core.config import settings
from .users import router as user_router
from .games import router as game_router
from .teams import router as team_router
from .tournament import router as tournament_router
from .match import router as match_router
from .map import router as map_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(router=user_router)
router.include_router(router=game_router)
router.include_router(router=team_router)
router.include_router(router=tournament_router)
router.include_router(router=match_router)
router.include_router(router=map_router)
