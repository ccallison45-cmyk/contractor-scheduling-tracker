# Tasks: contractor-scheduling-tracker

## Milestone 1: Project Setup

- [x] **Initialize project structure** [P0] [S] *(completed 2026-02-19)*
  - Description: Create folder layout, initialize pyproject.toml with uv, configure Ruff
  - Acceptance criteria: `uv sync` and `uv run ruff check .` run without errors

- [x] **Configure development environment** [P0] [S] *(completed 2026-02-19)*
  - Description: Create .gitignore, .env.example, verify local run instructions
  - Acceptance criteria: New developer can clone and run the app with only README instructions

- [x] **Set up testing framework** [P0] [S] *(completed 2026-02-19)*
  - Description: Configure pytest, create conftest.py with test client fixture, write smoke tests
  - Acceptance criteria: `uv run pytest` runs and passes

- [x] **Create CI pipeline** [P1] [S] *(completed 2026-02-19)*
  - Description: GitHub Actions workflow for Ruff lint and pytest on push/PR to main
  - Acceptance criteria: Pipeline config exists and is valid

## Milestone 2: Data Model and Seed Data

- [x] **Define SQLAlchemy models** [P0] [M] *(completed 2026-02-19)*
  - Description: Create Property, Contractor, Schedule, Payment ORM models with relationships and computed properties
  - Acceptance criteria: Models import without error; relationships resolve; computed properties work

- [x] **Set up database module** [P0] [S] *(completed 2026-02-19)*
  - Description: SQLAlchemy engine, session factory, Base, get_db dependency
  - Acceptance criteria: create_all() creates correct schema

- [x] **Implement seed data** [P0] [M] *(completed 2026-02-19)*
  - Description: 4 properties, 8 contractors, 14 schedules, 22 payments in seed.py
  - Acceptance criteria: App starts with empty DB; seed runs; all records queryable

## Milestone 3: Routes and Templates

- [x] **Create base template** [P0] [S] *(completed 2026-02-19)*
  - Description: Bootstrap 5 layout, navbar with active link detection, Demo badge, footer
  - Acceptance criteria: All pages extend base.html; navbar renders correctly

- [x] **Implement Dashboard** [P0] [M] *(completed 2026-02-19)*
  - Description: Summary cards, properties table with progress bars, recent payments
  - Acceptance criteria: Dashboard renders with correct aggregated numbers

- [x] **Implement Properties pages** [P0] [M] *(completed 2026-02-19)*
  - Description: Card grid with stage filter, detail page with stage pipeline and tabs
  - Acceptance criteria: All 4 properties appear; detail shows contractors and payments

- [x] **Implement Contractors pages** [P0] [M] *(completed 2026-02-19)*
  - Description: Searchable table, detail page with assignments and payment history tabs
  - Acceptance criteria: All 8 contractors shown; detail shows correct data

- [x] **Implement Schedule page** [P0] [M] *(completed 2026-02-19)*
  - Description: Property-grouped view with contractor assignment cards, active-only toggle
  - Acceptance criteria: Schedule renders; filtering works

- [x] **Implement Payments page** [P0] [M] *(completed 2026-02-19)*
  - Description: Summary stats, filterable table with color-coded rows, JS filters
  - Acceptance criteria: All payments appear; filters work; overdue rows highlighted

## Milestone 4: Polish and Deploy

- [x] **Add custom CSS** [P1] [S] *(completed 2026-02-19)*
  - Description: Stage pipeline styles, card hover effects, trade badge colors, progress bar thresholds
  - Acceptance criteria: Visually polished in browser

- [x] **Add health check endpoint** [P0] [S] *(completed 2026-02-19)*
  - Description: GET /health returns {"status": "ok", "demo": true}
  - Acceptance criteria: Endpoint responds with 200

- [ ] **Configure Railway deployment** [P0] [S]
  - Description: Create railway.toml, set env vars, connect GitHub, deploy
  - Acceptance criteria: App responds at Railway URL

- [ ] **Verify production environment** [P0] [S]
  - Description: Walk through all pages on live URL; verify seed data loaded
  - Acceptance criteria: Full demo walkthrough works on production URL

## Discovered During Work

(Add new tasks here as they are identified)
