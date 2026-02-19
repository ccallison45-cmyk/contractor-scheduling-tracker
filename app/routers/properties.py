from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Property

router = APIRouter(prefix="/properties")
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

STAGES = ["Purchased", "Demolition", "Rebuild", "Listed", "Sold"]


@router.get("")
async def properties_list(request: Request, db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return templates.TemplateResponse(
        "properties/list.html",
        {"request": request, "properties": properties, "stages": STAGES},
    )


@router.get("/{property_id}")
async def property_detail(property_id: int, request: Request, db: Session = Depends(get_db)):
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        return templates.TemplateResponse(
            "properties/list.html",
            {"request": request, "properties": [], "stages": STAGES, "error": "Property not found"},
        )

    # Determine completed stages for the pipeline
    stage_index = STAGES.index(prop.stage) if prop.stage in STAGES else 0

    return templates.TemplateResponse(
        "properties/detail.html",
        {
            "request": request,
            "property": prop,
            "stages": STAGES,
            "stage_index": stage_index,
        },
    )
