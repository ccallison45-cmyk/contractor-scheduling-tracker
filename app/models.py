from datetime import date, datetime

from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255))
    purchase_price: Mapped[float] = mapped_column(Numeric(12, 2))
    budget_total: Mapped[float] = mapped_column(Numeric(12, 2))
    stage: Mapped[str] = mapped_column(String(50))  # Purchased, Demolition, Rebuild, Listed, Sold
    purchase_date: Mapped[date] = mapped_column(Date)
    expected_completion: Mapped[date] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="proj")
    payments: Mapped[list["Payment"]] = relationship(back_populates="proj")

    @property
    def total_paid(self) -> float:
        return sum(float(p.amount) for p in self.payments if p.status == "Paid")

    @property
    def total_committed(self) -> float:
        return sum(float(p.amount) for p in self.payments)

    @property
    def budget_remaining(self) -> float:
        return float(self.budget_total) - self.total_committed

    @property
    def budget_percent_used(self) -> float:
        if float(self.budget_total) == 0:
            return 0
        return (self.total_committed / float(self.budget_total)) * 100

    @property
    def active_contractor_count(self) -> int:
        return sum(1 for s in self.schedules if s.status == "In Progress")

    @property
    def stage_badge_class(self) -> str:
        return {
            "Purchased": "secondary",
            "Demolition": "warning",
            "Rebuild": "primary",
            "Listed": "info",
            "Sold": "success",
        }.get(self.stage, "secondary")


class Contractor(Base):
    __tablename__ = "contractors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    contact_name: Mapped[str] = mapped_column(String(255))
    trade: Mapped[str] = mapped_column(String(100))
    hourly_rate: Mapped[float | None] = mapped_column(Numeric(8, 2), nullable=True)
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(255))
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="contractor")
    payments: Mapped[list["Payment"]] = relationship(back_populates="contractor")

    @property
    def total_paid(self) -> float:
        return sum(float(p.amount) for p in self.payments if p.status == "Paid")

    @property
    def active_assignment_count(self) -> int:
        return sum(1 for s in self.schedules if s.status == "In Progress")

    @property
    def trade_badge_class(self) -> str:
        return {
            "General Contractor": "dark",
            "Electrical": "warning",
            "Plumbing": "info",
            "HVAC": "secondary",
            "Roofing": "primary",
            "Landscaping": "success",
            "Interior Design": "danger",
            "Demolition": "dark",
        }.get(self.trade, "secondary")


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[int] = mapped_column(primary_key=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"))
    contractor_id: Mapped[int] = mapped_column(ForeignKey("contractors.id"))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    scope_of_work: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(50))  # Scheduled, In Progress, Completed, Cancelled

    proj: Mapped["Property"] = relationship(back_populates="schedules")
    contractor: Mapped["Contractor"] = relationship(back_populates="schedules")

    @property
    def status_badge_class(self) -> str:
        return {
            "Scheduled": "info",
            "In Progress": "primary",
            "Completed": "success",
            "Cancelled": "secondary",
        }.get(self.status, "secondary")


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"))
    contractor_id: Mapped[int] = mapped_column(ForeignKey("contractors.id"))
    amount: Mapped[float] = mapped_column(Numeric(12, 2))
    due_date: Mapped[date] = mapped_column(Date)
    paid_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(50))  # Pending, Paid, Overdue
    description: Mapped[str] = mapped_column(Text)
    invoice_number: Mapped[str] = mapped_column(String(50))

    proj: Mapped["Property"] = relationship(back_populates="payments")
    contractor: Mapped["Contractor"] = relationship(back_populates="payments")

    @property
    def is_overdue(self) -> bool:
        return self.status == "Overdue" or (
            self.due_date < datetime.now().date() and self.status == "Pending"
        )

    @property
    def status_badge_class(self) -> str:
        if self.is_overdue:
            return "danger"
        return {
            "Pending": "warning",
            "Paid": "success",
            "Overdue": "danger",
        }.get(self.status, "secondary")

    @property
    def row_class(self) -> str:
        if self.is_overdue:
            return "table-danger"
        if self.status == "Paid":
            return "table-success"
        return ""
