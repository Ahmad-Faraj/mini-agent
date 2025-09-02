# Mini-Agent: Log File Debugger (Next.js + FastAPI + Postgres)

Upload a log file → backend flags lines and returns a concise summary with suggested fixes.

## Stack

- Frontend: Next.js (deployed on Vercel)
- Backend: FastAPI (separate service)
- DB: Postgres (stores sessions/messages; optional for log mode)
- LLM: OpenAI (server-side only)

## Run locally (no Docker)

1) Frontend install

```bash
npm install
```

2) Backend deps

```bash
pip3 install --break-system-packages -r backend/requirements.txt
```

3) Environment

```bash
cp .env.example .env
# set OPENAI_API_KEY in .env (optional but recommended)
```

4) Start backend (SQLite by default)

```bash
bash backend/run.sh
# backend: http://localhost:8000
```

5) Start frontend

```bash
export NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev
# app: http://localhost:3000
```

## Run with Docker Compose

```bash
OPENAI_API_KEY=sk-... docker compose up --build
# backend: http://localhost:8000  |  postgres: localhost:5432 (app/app)
```

Apply SQL (optional; app auto-creates SQLite tables, Postgres uses SQL):

```bash
psql postgresql://app:app@localhost:5432/app -f db/migrations/0001_init.sql
```

## Deploy

- Frontend (Vercel):
  - Framework Preset: Next.js
  - Root Directory: `./`
  - Build Command: `npm run build`
  - Env: `NEXT_PUBLIC_API_URL=https://YOUR-BACKEND`

- Backend (Railway/Render/Fly):
  - Entrypoint: `bash backend/run.sh`
  - Env: `DATABASE_URL`, `OPENAI_API_KEY`, `CORS_ORIGINS=https://YOUR-VERCEL`

## Endpoints

- `POST /chat/log-analyze` (multipart file: `file`) → { flagged[], analysis }
- `POST /chat/sessions` → create session
- `GET /chat/sessions/{id}` → session with messages
- `POST /chat/sessions/{id}/message` → add message and get assistant reply
