from fastapi import APIRouter

from .auth import router as auth
from .user import router as user
from .rate import router as rate


router = APIRouter()
router.include_router(auth)
router.include_router(user)
router.include_router(rate)
