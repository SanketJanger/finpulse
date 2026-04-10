from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import get_logger, setup_logging


setup_logging(settings.APP_ENV, settings.APP_DEBUG)
logger = get_logger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.APP_DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def on_startup() -> None:
    logger.info("Application startup")


@app.on_event("shutdown")
async def on_shutdown() -> None:
    logger.info("Application shutdown")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.websocket("/ws/feed")
async def feed_websocket(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        await websocket.send_json({"status": "connected", "message": "Feed stream placeholder"})
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        logger.info("Feed websocket disconnected")
