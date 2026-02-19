# ADR-001: Initial Architecture and Tool Choices

## Status

Accepted

## Date

2026-02-19

## Context

Building a demo web app for a real estate developer client (Reinhard von Hollander) who manages property redevelopment projects. The app needs to track contractor schedules, payments, and budgets across multiple properties. It must look polished enough to demo in a client meeting, run online, and be easy to customize when real requirements arrive.

Key forces:
- Demo-quality UI needed (must look like a real production tool)
- No frontend build toolchain (keeps it simple for a solo developer)
- Needs a relational database for realistic demo data (properties → contractors → schedules → payments)
- Must match conventions of existing projects (Python, uv, FastAPI, Railway)
- Free-tier hosting required
- Easy to customize seed data when real requirements arrive

## Decision

### 1. Backend: Python 3.12 + FastAPI

- Server-rendered HTML pages using Jinja2 templates
- SQLAlchemy ORM for database access
- Auto-seeding demo data in FastAPI lifespan handler
- Package management via uv with pyproject.toml

### 2. Frontend: Jinja2 Templates + Bootstrap 5 (CDN)

- No separate frontend framework or build step
- Bootstrap 5 loaded from CDN for instant styling (cards, tables, badges, progress bars)
- Bootstrap Icons for UI iconography
- Minimal vanilla JavaScript only for client-side table filtering

### 3. Database: SQLite + SQLAlchemy ORM

- Single SQLite file (`contractor_tracker.db`)
- 4 models: Property, Contractor, Schedule, Payment
- Auto-created and seeded on first startup
- DATABASE_URL env var allows swapping to PostgreSQL with one config change

### 4. Deployment: Railway

- Auto-deploys from GitHub main branch
- railway.toml configures build and start command
- SQLite auto-seeds on every fresh deploy (ephemeral filesystem is acceptable for a demo)

## Alternatives Considered

### React/Vue frontend
- **Pros**: Rich interactivity, component reuse, modern developer experience
- **Cons**: Requires separate build step, adds complexity, two deployment targets
- **Why rejected**: A server-rendered demo with Bootstrap achieves the same visual impact without the build pipeline overhead. No real-time interactivity is needed.

### PostgreSQL database
- **Pros**: Production-grade, concurrent write support, managed service options
- **Cons**: Requires a managed database service with credentials, adds external dependency
- **Why rejected**: SQLite is sufficient for a single-user demo with < 200KB of data. The SQLAlchemy ORM makes PostgreSQL a one-line config swap when needed.

### Tailwind CSS
- **Pros**: Utility-first, highly customizable
- **Cons**: Requires a build step (PostCSS) or larger CDN bundle
- **Why rejected**: Bootstrap provides ready-made components (cards, tables, badges, progress bars) that directly match this UI's needs. No build step with the CDN approach.

## Consequences

### Positive
- No frontend build pipeline — straightforward Python-only development
- Auto-seeding means the demo always has realistic data, even after redeployment
- Easy handoff: a developer familiar with Python + FastAPI can modify any part of the app
- All seed data in one file (`app/seed.py`) makes customization straightforward

### Negative
- SQLite is not suitable for multi-user concurrent writes in production
- Jinja2 templates are not as interactive as a JS framework — no real-time updates
- Bootstrap CDN dependency (offline viewing requires caching)

### Mitigations
- Document PostgreSQL upgrade path (change DATABASE_URL only)
- Add minimal vanilla JS only where needed (payment filters, search)
- Pin Bootstrap CDN to specific version to prevent breaking changes
