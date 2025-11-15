from fastapi import APIRouter

from core.auth.helper import helper_jwt as helper_jwt
from core.auth.views import router as auth_views_router

router = APIRouter()
router.include_router(auth_views_router)
router.include_router(auth_views_router)
