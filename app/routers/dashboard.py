from datetime import date, timedelta
from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Contractor, Payment, Property, Schedule

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


@router.get("/")
async def dashboard(request: Request, db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    active_properties = [p for p in properties if p.stage != "Sold"]

    # Summary stats
    active_count = len(active_properties)
    total_committed = sum(p.total_committed for p in properties)
    total_paid = sum(p.total_paid for p in properties)

    # Payments due this month
    today = date.today()
    first_of_month = today.replace(day=1)
    if today.month == 12:
        last_of_month = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
    else:
        last_of_month = today.replace(month=today.month + 1, day=1) - timedelta(days=1)

    payments_due_month = (
        db.query(Payment)
        .filter(
            Payment.due_date >= first_of_month,
            Payment.due_date <= last_of_month,
            Payment.status != "Paid",
        )
        .all()
    )
    payments_due_count = len(payments_due_month)
    payments_due_amount = sum(float(p.amount) for p in payments_due_month)

    # Active contractors
    active_contractors = (
        db.query(Contractor)
        .join(Schedule)
        .filter(Schedule.status == "In Progress")
        .distinct()
        .count()
    )

    # Overdue payments
    overdue_payments = db.query(Payment).filter(Payment.status == "Overdue").all()
    overdue_count = len(overdue_payments)
    overdue_amount = sum(float(p.amount) for p in overdue_payments)

    # Recent payments (last 5 by due date)
    recent_payments = (
        db.query(Payment).order_by(Payment.due_date.desc()).limit(5).all()
    )

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "properties": properties,
            "active_properties": active_properties,
            "active_count": active_count,
            "total_committed": total_committed,
            "total_paid": total_paid,
            "payments_due_count": payments_due_count,
            "payments_due_amount": payments_due_amount,
            "active_contractors": active_contractors,
            "overdue_count": overdue_count,
            "overdue_amount": overdue_amount,
            "recent_payments": recent_payments,
        },
    )
