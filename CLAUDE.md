# CLAUDE.md — contractor-scheduling-tracker

## Project Identity

- **Name**: contractor-scheduling-tracker
- **Description**: Web app for tracking contractor schedules, payments, and budgets across real estate development projects
- **Primary Language**: Python
- **Interaction Model**: Server-rendered web app (FastAPI + Jinja2 templates), browser-only
- **Repository**: local (to be pushed to GitHub)

## Tooling & System Map

Every tool in this project was selected using the Tool Selection Rules. No tool is here "by default."

| Tool | Category | Why Selected | Scope of Use | Data Allowed | Risks | Mitigations |
|---|---|---|---|---|---|---|
| Python 3.12 | Language | Backend API + data modeling; owner comfortable with Python; matches existing project pattern | All backend code: routes, models, seed data, tests | Property/contractor/payment records (fictional demo data) | Dependency management | uv for lockfile, pin versions in pyproject.toml |
| FastAPI | Web Framework | Python + web UI trigger; serves HTML pages via Jinja2 and JSON health endpoint | Route handlers, form submissions, page rendering | All app data | Template rendering overhead | Keep templates simple; Jinja2 auto-escaping enabled |
| Jinja2 | Templating | Server-side HTML rendering; no frontend build step; ships with FastAPI | All HTML page templates | Page-scoped data dicts | None significant | Escape all user input; use auto-escaping |
| Bootstrap 5 | CSS Framework | CDN delivery, no build step, polished grid/components for demo | All page layouts and UI components | None (CDN only) | CDN availability | Pin to specific Bootstrap version URL |
| SQLite + SQLAlchemy | Database/ORM | Single-user demo, < 1MB data, no concurrent writes; ORM gives clean model definitions | All persistent data: properties, contractors, schedules, payments | All application records | File-based; not suitable for high concurrency | Acceptable for demo; upgrade path to PostgreSQL documented |
| uv | Package Manager | Consistent with existing projects; fast, deterministic lockfile | Dependency resolution and virtual environment | Source code only | None significant | Pin version in CI |
| pytest | Testing | Python project auto-selects pytest | All backend test files | Test fixtures only | None significant | Keep tests fast |
| Ruff | Linting | Python project auto-selects Ruff | All Python files | Source code only | None significant | Pin version |
| GitHub Actions | CI/CD | GitHub-hosted repo, standard choice | Lint + test on push/PR | Source code, test results | Free tier limits | Minimal pipeline |
| Railway | Deployment | Free-tier PaaS; auto-deploys from GitHub | Production hosting | All application data | SQLite on ephemeral filesystem | Auto-seed on startup; volume mount for persistence |

## When to Use Python

Python is the primary language for this project. Use it for:
- All backend API code (FastAPI routes, request handling, template rendering)
- SQLAlchemy ORM models and database operations
- Seed data loading and database initialization
- Tests (pytest)
- Utility scripts

Do NOT use Python for:
- CSS styling — use Bootstrap 5 via CDN
- Client-side interactivity — use minimal vanilla JavaScript only (filter dropdowns, search)

Python version: 3.12+
Package manager: uv (with pyproject.toml)

## When to Use MCP

MCP is **not used** in this project. No MCP servers are configured or authorized.

If a future need arises:
1. Document the need in an ADR.
2. Verify all activation criteria from the MCP Policy.
3. Update this CLAUDE.md with the allowed servers table.

## Commands

```bash
# Install dependencies
uv sync

# Start development server
uv run uvicorn app.main:app --reload --port 8000

# Run tests
uv run pytest

# Run linter/formatter
uv run ruff check . && uv run ruff format .
```

Production deployment happens via Git push — Railway auto-deploys from the main branch.

## Invariants

These must **always** be true. Violating any invariant is a blocking issue.

1. The database must be seeded with realistic demo data on first startup if the database file does not exist.
2. All pages must render without error when the seed data is present.
3. No real contractor names, addresses, or financial data may appear in the codebase — use fictional data only.
4. All tests pass before any merge to main.
5. No secrets in code, config files, or logs.
6. `.env.example` stays in sync with actual environment variables used.

## How Future Chats Must Behave

When working in this project, you (Claude or any AI assistant) must:

1. **Read this CLAUDE.md first** before making any changes.
2. **Follow the Tooling & System Map.** Do not introduce tools not listed in the table without creating an ADR and updating this file.
3. **Respect the invariants.** If a proposed change would violate an invariant, stop and flag it.
4. **Use the specified language.** Python for backend, JavaScript for client-side interactivity only. Do not switch without justification.
5. **Run tests after changes.** Use `uv run pytest`. Do not skip.
6. **Do not commit secrets.** Check `.env.example` for the pattern. Real values go in `.env` (gitignored).
7. **Keep TASKS.md updated.** Mark tasks complete as you finish them. Add new tasks as discovered.
8. **Create ADRs for significant decisions.** Any new tool, major refactor, or architecture change gets an ADR in `docs/decisions/`.
9. **Prefer editing over creating.** Modify existing files rather than creating new ones, unless the change is clearly a new module.
10. **Ask when uncertain.** If requirements are ambiguous, ask rather than assume.
