from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class MessageCreate(BaseModel):
    role: str
    content: str


class MessageRead(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class SessionCreate(BaseModel):
    title: Optional[str] = None


class SessionRead(BaseModel):
    id: str
    title: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class SessionWithMessages(SessionRead):
    messages: List[MessageRead]

