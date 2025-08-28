from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.db.session import engine
from backend.app.models.base import Base
from backend.app.routers.chat import router as chat_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create tables for SQLite/dev mode
    Base.metadata.create_all(bind=engine)

    app.include_router(chat_router)

    @app.get("/")
    def root():
        return {"status": "ok", "app": settings.app_name, "env": settings.environment}

    return app


app = create_app()

