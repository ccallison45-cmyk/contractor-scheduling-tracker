# Local Development

## Prerequisites

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/) package manager
- Git

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd contractor-scheduling-tracker

# Install dependencies
uv sync

# Copy environment file
cp .env.example .env
```

## Running the Application

```bash
uv run uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

On first startup, the database is automatically created and seeded with demo data. You should see the dashboard with 4 properties, 8 contractors, and payment data.

## Database

The SQLite database file (`contractor_tracker.db`) is created automatically. To reset the database:

```bash
# Delete the database file and restart the app
rm contractor_tracker.db
uv run uvicorn app.main:app --reload --port 8000
```

The seed script will recreate all demo data on startup.

## Running Tests

```bash
uv run pytest
```

Tests use a separate SQLite database (`test_contractor_tracker.db`) that is created and destroyed for each test run.

## Linting

```bash
# Check for issues
uv run ruff check .

# Auto-format
uv run ruff format .
```

## Common Issues

| Issue | Cause | Fix |
|---|---|---|
| Port 8000 already in use | Another process on the port | Use `--port 8001` or kill the other process |
| Database not seeding | `contractor_tracker.db` already exists with data | Delete the file and restart |
| Import errors | Dependencies not installed | Run `uv sync` |
| Template not found errors | Working directory mismatch | Run uvicorn from the project root |
| Tests fail with DB errors | Stale test database | Delete `test_contractor_tracker.db` and rerun |
