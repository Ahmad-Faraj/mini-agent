from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os

from backend.app.core.config import settings


def _build_database_url() -> str:
    if settings.database_url:
        return settings.database_url
    # Dev fallback: local SQLite file to enable running without Postgres
    default_sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../dev.sqlite3"))
    return f"sqlite:///{default_sqlite_path}"


DATABASE_URL = _build_database_url()

# For SQLite we need check_same_thread=False
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

