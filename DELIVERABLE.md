# Mini-Agent – Deliverable

## Idea and Why
For this challenge, I built a **chat-based mini agent** that can handle simple coding and testing tasks. It has a minimal chat UI, a Python backend with FastAPI, and a Postgres database that stores all interactions.  

I went with this idea because it’s both **useful and extendable**. A lot of developers (myself included) need a quick helper to generate snippets, suggest tests, or debug small pieces of code. Starting with a small but working base means I can expand it later into something more powerful (like log file debugging or data analysis).  

---

## Tools I Used (and Why)
- **FastAPI (Python)** – quick to set up, async support, and auto docs are very handy.  
- **Next.js + Tailwind** – easy way to get a simple chat UI working without wasting time on design.  
- **Postgres** – reliable for storing interactions, and I wanted proper SQL instead of just JSON files.  
- **Docker + docker-compose** – so the whole thing can be spun up with one command.  
- **Neovim** – my main editor; I prefer it for speed and focus while hacking on projects like this.  

I chose these because they let me move fast while showing I’m comfortable across the stack.

---

## Architecture
- **Frontend (Next.js)** → chat interface with a textbox + history.  
- **Backend (FastAPI)** → two endpoints: `/chat` for sending messages and `/history` for fetching past ones.  
- **Database (Postgres)** → single table (`interactions`) to log prompts and responses.  

Flow is straightforward: frontend sends a message → backend stores it → calls the LLM → saves the response → returns it to the UI.

---

## Time Spent
- Planning and setup: ~3–4 hours  
- Backend (FastAPI + DB integration): ~6 hours  
- Frontend (Next.js chat page): ~4 hours  
- Docker & testing: ~2 hours  
- Docs + demo prep: ~2 hours  

Roughly ~18 hours total spread across three days.

---

## If I Had More Time
- Add **file uploads** (like logs or CSVs) so the agent can analyze them.  
- Make the responses **stream in real time** instead of waiting for the full output.  
- Add a quick **GitHub login** for basic auth.  
- Deploy to something like Railway/Render for a live demo link.  
- Experiment with **RAG (retrieval-augmented generation)** using docs from libraries like FastAPI or Pandas.  

---

## Vision Beyond MVP
The current version is intentionally minimal, but the structure makes it easy to grow. My goal would be to turn it into a small “Swiss Army knife” for developers: a single agent that can generate tests, read logs, and help deploy small projects — all accessible through the same chat interface.

---
