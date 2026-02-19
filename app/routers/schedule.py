from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import Property, Schedule

router = APIRouter(prefix="/schedule")
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

STAGE_ORDER = {"Purchased": 0, "Demolition": 1, "Rebuild": 2, "Listed": 3, "Sold": 4}


@router.get("")
async def schedule_view(request: Request, db: Session = Depends(get_db)):
    properties = (
        db.query(Property)
        .options(joinedload(Property.schedules).joinedload(Schedule.contractor))
        .all()
    )
    # Sort by stage order
    properties.sort(key=lambda p: STAGE_ORDER.get(p.stage, 99))

    return templates.TemplateResponse(
        "schedule.html",
        {"request": request, "properties": properties},
    )
