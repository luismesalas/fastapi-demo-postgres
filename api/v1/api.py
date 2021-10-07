from fastapi import APIRouter

from api.v1.routers import health, sports_facilities


def get_api():
    api_router = APIRouter()
    api_router.include_router(health.router)
    api_router.include_router(sports_facilities.router, prefix="/sports-facilities")
    return api_router
