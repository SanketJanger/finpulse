from fastapi import APIRouter


feed_router = APIRouter(prefix="/feed", tags=["feed"])
search_router = APIRouter(prefix="/search", tags=["search"])
alerts_router = APIRouter(prefix="/alerts", tags=["alerts"])
trending_router = APIRouter(prefix="/trending", tags=["trending"])


@feed_router.get("")
async def get_feed() -> dict[str, list]:
    return {"items": []}


@search_router.post("")
async def search_news() -> dict[str, list]:
    return {"results": []}


@alerts_router.get("")
async def get_alerts() -> dict[str, list]:
    return {"alerts": []}


@trending_router.get("")
async def get_trending() -> dict[str, list]:
    return {"topics": []}


api_router = APIRouter()
api_router.include_router(feed_router)
api_router.include_router(search_router)
api_router.include_router(alerts_router)
api_router.include_router(trending_router)
