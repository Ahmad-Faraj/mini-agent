from __future__ import annotations

from typing import List, Dict, Any
import os
import httpx
from openai import OpenAI

from backend.app.core.config import settings


def _format_messages(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    formatted: List[Dict[str, str]] = []
    for item in history:
        role = item.get("role", "user")
        content = item.get("content", "")
        formatted.append({"role": role, "content": content})
    return formatted


async def chat_complete(history: List[Dict[str, str]]) -> str:
    # Prefer OpenAI, fallback to Ollama if configured, else simple heuristic echo
    if settings.openai_api_key:
        client = OpenAI(api_key=settings.openai_api_key)
        msgs = _format_messages(history)
        # Ensure system prompt
        if not any(m["role"] == "system" for m in msgs):
            msgs.insert(0, {"role": "system", "content": "You are a helpful, concise coding and data assistant."})
        try:
            resp = client.chat.completions.create(model=settings.openai_model, messages=msgs, temperature=0.3)
            return resp.choices[0].message.content or ""
        except Exception as exc:
            return f"[LLM error: {exc}]"

    if settings.ollama_base_url:
        try:
            async with httpx.AsyncClient(base_url=settings.ollama_base_url, timeout=60) as http:
                payload = {"model": settings.ollama_model, "messages": _format_messages(history), "stream": False}
                r = await http.post("/api/chat", json=payload)
                r.raise_for_status()
                data = r.json()
                # Ollama returns {message: {content: str}} or similar depending on version
                msg = data.get("message") or {}
                return msg.get("content", "")
        except Exception as exc:
            return f"[Ollama error: {exc}]"

    # Fallback heuristic: simple echo with tip
    last_user = next((m["content"] for m in reversed(history) if m.get("role") == "user"), "")
    return f"You said: {last_user}\n\n(Add OPENAI_API_KEY to use a real model.)"

