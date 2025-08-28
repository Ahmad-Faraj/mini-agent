#!/usr/bin/env bash
set -euo pipefail

export PYTHONUNBUFFERED=1

if [ -f "../.env" ]; then
  set -a
  source ../.env
  set +a
fi

exec python3 -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload

