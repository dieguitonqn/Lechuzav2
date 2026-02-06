from fastapi import APIRouter
from .endpoints.login import router as login_router

auth_router = APIRouter()

# Include all auth endpoints
auth_router.include_router(login_router, prefix="/auth", tags=["auth"])