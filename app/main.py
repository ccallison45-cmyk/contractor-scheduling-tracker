import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import Base, SessionLocal, engine
from app.routers import contractors, dashboard, payments, properties, schedule
from app.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="Contractor Scheduling & Payment Tracker",
    description="Demo app for real estate development project management",
    lifespan=lifespan,
)

app_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=app_dir / "static"), name="static")

templates = Jinja2Templates(directory=app_dir / "templates")


@app.get("/health")
async def health_check():
    return JSONResponse({"status": "ok", "demo": True})


app.include_router(dashboard.router)
app.include_router(properties.router)
app.include_router(contractors.router)
app.include_router(schedule.router)
app.include_router(payments.router)


def get_demo_mode() -> bool:
    return os.getenv("DEMO_MODE", "true").lower() == "true"


@app.middleware("http")
async def add_demo_mode(request: Request, call_next):
    request.state.demo_mode = get_demo_mode()
    response = await call_next(request)
    return response
