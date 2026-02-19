from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import Contractor, Payment, Property

router = APIRouter(prefix="/payments")
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("")
async def payments_list(request: Request, db: Session = Depends(get_db)):
    payments = (
        db.query(Payment)
        .options(joinedload(Payment.proj), joinedload(Payment.contractor))
        .order_by(Payment.due_date.desc())
        .all()
    )

    # Summary stats
    total_paid = sum(float(p.amount) for p in payments if p.status == "Paid")
    total_pending = sum(float(p.amount) for p in payments if p.status == "Pending")
    total_overdue = sum(float(p.amount) for p in payments if p.status == "Overdue")

    # Get unique properties and contractors for filter dropdowns
    properties = db.query(Property).all()
    contractors = db.query(Contractor).all()

    return templates.TemplateResponse(
        "payments.html",
        {
            "request": request,
            "payments": payments,
            "total_paid": total_paid,
            "total_pending": total_pending,
            "total_overdue": total_overdue,
            "properties": properties,
            "contractors": contractors,
        },
    )
