from fastapi import APIRouter

from .public.user_routes import router as user_router

api_router = APIRouter()

api_router.include_router(prefix="/users", tags=["users"], router=user_router)
