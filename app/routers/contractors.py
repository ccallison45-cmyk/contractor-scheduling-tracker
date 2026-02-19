from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Contractor

router = APIRouter(prefix="/contractors")
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("")
async def contractors_list(request: Request, db: Session = Depends(get_db)):
    contractors = db.query(Contractor).all()
    return templates.TemplateResponse(
        "contractors/list.html",
        {"request": request, "contractors": contractors},
    )


@router.get("/{contractor_id}")
async def contractor_detail(contractor_id: int, request: Request, db: Session = Depends(get_db)):
    contractor = db.query(Contractor).filter(Contractor.id == contractor_id).first()
    if not contractor:
        return templates.TemplateResponse(
            "contractors/list.html",
            {"request": request, "contractors": [], "error": "Contractor not found"},
        )
    return templates.TemplateResponse(
        "contractors/detail.html",
        {"request": request, "contractor": contractor},
    )
