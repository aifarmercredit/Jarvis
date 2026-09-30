from fastapi import FastAPI
from app.api.routes import router
from app.api.websocket import websocket_endpoint

def create_app() -> FastAPI:
    app = FastAPI(title="JARVIS AI Assistant", version="0.1.0")
    app.include_router(router, prefix="/api")
    app.add_api_websocket_route("/api/ws", websocket_endpoint)
    return app
