# Contractor Scheduling & Payment Tracker

Web app for tracking contractor schedules, payments, and budgets across real estate development projects. Built as a demo for Reinhard von Hollander.

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
git clone <repo-url>
cd contractor-scheduling-tracker
uv sync
cp .env.example .env
```

### Running

```bash
uv run uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000). The database auto-seeds with demo data on first startup.

## Architecture

```
Browser
   │
   ▼
FastAPI (app/main.py)
   ├── Jinja2 templates (server-rendered HTML)
   ├── Bootstrap 5 (CDN, no build step)
   ├── Static files (custom.css)
   │
   ├── Routers
   │     dashboard.py    GET /
   │     properties.py   GET /properties, /properties/{id}
   │     contractors.py  GET /contractors, /contractors/{id}
   │     schedule.py     GET /schedule
   │     payments.py     GET /payments
   │
   ▼
SQLAlchemy ORM (app/models.py)
   │
   ▼
SQLite (contractor_tracker.db, auto-seeded)
```

### Key Components

| Component | Purpose | Location |
|---|---|---|
| Models | Property, Contractor, Schedule, Payment ORM definitions | `app/models.py` |
| Seed Data | Pre-loaded demo data (4 properties, 8 contractors, 22 payments) | `app/seed.py` |
| Templates | Jinja2 HTML templates with Bootstrap 5 | `app/templates/` |
| Routers | FastAPI route handlers per page | `app/routers/` |

### Data Flow

1. FastAPI starts → lifespan handler creates tables and seeds database if empty
2. User visits a page → router queries database via SQLAlchemy
3. Router passes data to Jinja2 template → server-rendered HTML returned
4. Minimal vanilla JS handles client-side filtering (payments page)

## Development

### Setup

```bash
uv sync --extra dev
cp .env.example .env
```

### Testing

```bash
uv run pytest
```

### Code Style

```bash
uv run ruff check . && uv run ruff format .
```

### Project Structure

```
contractor-scheduling-tracker/
  app/
    main.py              # FastAPI app entry point
    database.py          # SQLAlchemy engine and session
    models.py            # ORM models
    seed.py              # Demo data seeding
    routers/             # Route handlers
    templates/           # Jinja2 HTML templates
    static/              # CSS
  tests/                 # pytest test suite
  docs/
    decisions/           # Architecture Decision Records
    runbooks/            # Operational guides
```

## Deployment

Deployed to Railway. Auto-deploys from the `main` branch.

### Environment Variables

| Variable | Description | Default |
|---|---|---|
| `APP_ENV` | Environment name | `development` |
| `APP_PORT` | Server port | `8000` |
| `DATABASE_URL` | SQLite connection string | `sqlite:///./contractor_tracker.db` |
| `DEMO_MODE` | Show "Demo" banner in navbar | `true` |

### Deploy to Railway

1. Push code to GitHub
2. Connect repo in Railway dashboard
3. Set environment variables
4. Railway auto-builds and deploys via `railway.toml`
