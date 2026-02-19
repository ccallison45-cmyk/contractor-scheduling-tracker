from datetime import date

from sqlalchemy.orm import Session

from app.models import Contractor, Payment, Property, Schedule


def seed_database(db: Session) -> None:
    """Seed the database with realistic demo data. Only runs if tables are empty."""
    if db.query(Property).first() is not None:
        return

    # --- Properties ---
    p1 = Property(
        address="1247 Birchwood Avenue, Denver, CO 80218",
        purchase_price=485000,
        budget_total=310000,
        stage="Rebuild",
        purchase_date=date(2025, 7, 14),
        expected_completion=date(2026, 5, 30),
        notes=(
            "Single-family, 1960s ranch. Full gut rehab"
            " — new roof, HVAC, updated kitchen and baths."
        ),
    )
    p2 = Property(
        address="3892 Fairview Lane, Lakewood, CO 80214",
        purchase_price=395000,
        budget_total=420000,
        stage="Demolition",
        purchase_date=date(2025, 10, 22),
        expected_completion=date(2026, 8, 15),
        notes=(
            "Corner lot, existing structure being demolished."
            " New construction — 3-bed/2.5-bath modern."
        ),
    )
    p3 = Property(
        address="712 Maple Street, Aurora, CO 80010",
        purchase_price=310000,
        budget_total=280000,
        stage="Purchased",
        purchase_date=date(2026, 1, 8),
        expected_completion=date(2026, 11, 30),
        notes="Just closed. Awaiting permits. Kitchen/bath remodel.",
    )
    p4 = Property(
        address="5501 Cottonwood Drive, Englewood, CO 80110",
        purchase_price=445000,
        budget_total=265000,
        stage="Listed",
        purchase_date=date(2025, 3, 1),
        expected_completion=date(2025, 12, 20),
        notes="Rehab complete. Listed at $875,000. Showing scheduled.",
    )
    db.add_all([p1, p2, p3, p4])
    db.flush()

    # --- Contractors ---
    c1 = Contractor(
        name="Apex General Contracting",
        contact_name="Marcus Webb",
        trade="General Contractor",
        hourly_rate=85,
        phone="(720) 555-0142",
        email="marcus@apexgc-denver.com",
    )
    c2 = Contractor(
        name="Volta Electric LLC",
        contact_name="Diane Kowalski",
        trade="Electrical",
        hourly_rate=95,
        phone="(720) 555-0287",
        email="diane@voltaelectric.com",
    )
    c3 = Contractor(
        name="Rocky Mountain Plumbing",
        contact_name="Tom Brandt",
        trade="Plumbing",
        hourly_rate=90,
        phone="(303) 555-0193",
        email="tom@rmpplumbing.com",
    )
    c4 = Contractor(
        name="Summit HVAC Services",
        contact_name="Priya Nair",
        trade="HVAC",
        hourly_rate=110,
        phone="(720) 555-0341",
        email="priya@summithvac.com",
    )
    c5 = Contractor(
        name="Peak Roofing Co.",
        contact_name="Jesse Flores",
        trade="Roofing",
        hourly_rate=75,
        phone="(303) 555-0457",
        email="jesse@peakroofing.com",
    )
    c6 = Contractor(
        name="Front Range Demolition",
        contact_name="Bill Hargrove",
        trade="Demolition",
        hourly_rate=None,
        phone="(303) 555-0512",
        email="bill@frontrangedemo.com",
        notes="Fixed-bid projects only.",
    )
    c7 = Contractor(
        name="Greenleaf Landscaping",
        contact_name="Sandra Park",
        trade="Landscaping",
        hourly_rate=65,
        phone="(720) 555-0619",
        email="sandra@greenleafco.com",
    )
    c8 = Contractor(
        name="Novo Interiors",
        contact_name="Claire Dubois",
        trade="Interior Design",
        hourly_rate=120,
        phone="(720) 555-0734",
        email="claire@novointeriors.com",
    )
    db.add_all([c1, c2, c3, c4, c5, c6, c7, c8])
    db.flush()

    # --- Schedules ---
    # Property 1 — Birchwood Ave (Rebuild)
    schedules = [
        Schedule(
            property_id=p1.id,
            contractor_id=c1.id,
            start_date=date(2025, 9, 1),
            end_date=date(2026, 5, 30),
            scope_of_work="General oversight, framing, drywall",
            status="In Progress",
        ),
        Schedule(
            property_id=p1.id,
            contractor_id=c2.id,
            start_date=date(2025, 10, 15),
            end_date=date(2026, 2, 28),
            scope_of_work="Full electrical rewire, panel upgrade",
            status="In Progress",
        ),
        Schedule(
            property_id=p1.id,
            contractor_id=c3.id,
            start_date=date(2025, 11, 1),
            end_date=date(2026, 3, 15),
            scope_of_work="Rough-in and finish plumbing, two baths",
            status="In Progress",
        ),
        Schedule(
            property_id=p1.id,
            contractor_id=c4.id,
            start_date=date(2026, 1, 15),
            end_date=date(2026, 3, 30),
            scope_of_work="New forced-air system installation",
            status="Scheduled",
        ),
        Schedule(
            property_id=p1.id,
            contractor_id=c5.id,
            start_date=date(2025, 9, 10),
            end_date=date(2025, 10, 5),
            scope_of_work="Full roof replacement, architectural shingles",
            status="Completed",
        ),
        Schedule(
            property_id=p1.id,
            contractor_id=c8.id,
            start_date=date(2026, 2, 15),
            end_date=date(2026, 5, 15),
            scope_of_work="Kitchen and master bath design and finish",
            status="Scheduled",
        ),
        # Property 2 — Fairview Lane (Demolition)
        Schedule(
            property_id=p2.id,
            contractor_id=c6.id,
            start_date=date(2026, 1, 20),
            end_date=date(2026, 3, 10),
            scope_of_work="Full demolition, debris removal, site prep",
            status="In Progress",
        ),
        Schedule(
            property_id=p2.id,
            contractor_id=c1.id,
            start_date=date(2026, 3, 15),
            end_date=date(2026, 5, 1),
            scope_of_work="Site prep and foundation work post-demo",
            status="Scheduled",
        ),
        # Property 3 — Maple Street (Purchased)
        Schedule(
            property_id=p3.id,
            contractor_id=c1.id,
            start_date=date(2026, 2, 15),
            end_date=date(2026, 3, 31),
            scope_of_work="Initial assessment and permit coordination",
            status="Scheduled",
        ),
        # Property 4 — Cottonwood Drive (Listed, all completed)
        Schedule(
            property_id=p4.id,
            contractor_id=c1.id,
            start_date=date(2025, 4, 1),
            end_date=date(2025, 11, 30),
            scope_of_work="Kitchen remodel, flooring, paint",
            status="Completed",
        ),
        Schedule(
            property_id=p4.id,
            contractor_id=c2.id,
            start_date=date(2025, 5, 1),
            end_date=date(2025, 6, 15),
            scope_of_work="Kitchen electrical update, lighting",
            status="Completed",
        ),
        Schedule(
            property_id=p4.id,
            contractor_id=c3.id,
            start_date=date(2025, 5, 15),
            end_date=date(2025, 7, 1),
            scope_of_work="Kitchen and bath plumbing update",
            status="Completed",
        ),
        Schedule(
            property_id=p4.id,
            contractor_id=c5.id,
            start_date=date(2025, 4, 15),
            end_date=date(2025, 4, 20),
            scope_of_work="Roof inspection and minor repairs",
            status="Completed",
        ),
        Schedule(
            property_id=p4.id,
            contractor_id=c7.id,
            start_date=date(2025, 10, 1),
            end_date=date(2025, 11, 15),
            scope_of_work="Front/back yard redesign for curb appeal",
            status="Completed",
        ),
    ]
    db.add_all(schedules)

    # --- Payments ---
    payments = [
        # Property 4 — Cottonwood Drive (all paid, completed)
        Payment(
            property_id=p4.id,
            contractor_id=c1.id,
            amount=45000,
            due_date=date(2025, 6, 1),
            paid_date=date(2025, 6, 3),
            status="Paid",
            description="Kitchen remodel Phase 1",
            invoice_number="INV-2025-0012",
        ),
        Payment(
            property_id=p4.id,
            contractor_id=c1.id,
            amount=38000,
            due_date=date(2025, 9, 1),
            paid_date=date(2025, 9, 5),
            status="Paid",
            description="Kitchen remodel Phase 2 + flooring",
            invoice_number="INV-2025-0031",
        ),
        Payment(
            property_id=p4.id,
            contractor_id=c2.id,
            amount=12400,
            due_date=date(2025, 7, 1),
            paid_date=date(2025, 7, 8),
            status="Paid",
            description="Kitchen electrical and lighting",
            invoice_number="INV-2025-0017",
        ),
        Payment(
            property_id=p4.id,
            contractor_id=c3.id,
            amount=14800,
            due_date=date(2025, 8, 1),
            paid_date=date(2025, 8, 12),
            status="Paid",
            description="Kitchen and bath plumbing",
            invoice_number="INV-2025-0024",
        ),
        Payment(
            property_id=p4.id,
            contractor_id=c5.id,
            amount=3200,
            due_date=date(2025, 5, 1),
            paid_date=date(2025, 5, 2),
            status="Paid",
            description="Roof inspection and repairs",
            invoice_number="INV-2025-0008",
        ),
        Payment(
            property_id=p4.id,
            contractor_id=c7.id,
            amount=18500,
            due_date=date(2025, 11, 20),
            paid_date=date(2025, 11, 22),
            status="Paid",
            description="Full landscaping package",
            invoice_number="INV-2025-0058",
        ),
        # Property 1 — Birchwood Ave (mix of paid/pending/overdue)
        Payment(
            property_id=p1.id,
            contractor_id=c5.id,
            amount=28500,
            due_date=date(2025, 10, 10),
            paid_date=date(2025, 10, 15),
            status="Paid",
            description="Full roof replacement",
            invoice_number="INV-2025-0041",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c1.id,
            amount=35000,
            due_date=date(2025, 11, 1),
            paid_date=date(2025, 11, 8),
            status="Paid",
            description="Framing and rough-in work",
            invoice_number="INV-2025-0049",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c2.id,
            amount=18000,
            due_date=date(2025, 12, 15),
            paid_date=date(2025, 12, 20),
            status="Paid",
            description="Electrical rough-in, Phase 1",
            invoice_number="INV-2025-0062",
        ),
        # Overdue payments (Birchwood)
        Payment(
            property_id=p1.id,
            contractor_id=c3.id,
            amount=8900,
            due_date=date(2026, 1, 31),
            paid_date=None,
            status="Overdue",
            description="Drain rough-in",
            invoice_number="INV-2026-0003",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c1.id,
            amount=15000,
            due_date=date(2026, 1, 15),
            paid_date=None,
            status="Overdue",
            description="Interim milestone payment",
            invoice_number="INV-2026-0001",
        ),
        # Pending payments (Birchwood)
        Payment(
            property_id=p1.id,
            contractor_id=c3.id,
            amount=22500,
            due_date=date(2026, 2, 28),
            paid_date=None,
            status="Pending",
            description="Rough-in plumbing complete",
            invoice_number="INV-2026-0008",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c2.id,
            amount=14500,
            due_date=date(2026, 3, 15),
            paid_date=None,
            status="Pending",
            description="Electrical finish work",
            invoice_number="INV-2026-0014",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c1.id,
            amount=42000,
            due_date=date(2026, 4, 1),
            paid_date=None,
            status="Pending",
            description="Drywall and interior completion",
            invoice_number="INV-2026-0021",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c4.id,
            amount=31000,
            due_date=date(2026, 3, 30),
            paid_date=None,
            status="Pending",
            description="HVAC system install",
            invoice_number="INV-2026-0019",
        ),
        Payment(
            property_id=p1.id,
            contractor_id=c8.id,
            amount=25000,
            due_date=date(2026, 4, 15),
            paid_date=None,
            status="Pending",
            description="Design and finish materials",
            invoice_number="INV-2026-0023",
        ),
        # Property 2 — Fairview Lane (Demolition)
        Payment(
            property_id=p2.id,
            contractor_id=c6.id,
            amount=48000,
            due_date=date(2026, 3, 10),
            paid_date=None,
            status="Pending",
            description="Full demolition and site clearance",
            invoice_number="INV-2026-0011",
        ),
        Payment(
            property_id=p2.id,
            contractor_id=c1.id,
            amount=25000,
            due_date=date(2026, 4, 15),
            paid_date=None,
            status="Pending",
            description="Foundation work deposit",
            invoice_number="INV-2026-0025",
        ),
        # Property 3 — Maple Street (Purchased)
        Payment(
            property_id=p3.id,
            contractor_id=c1.id,
            amount=5500,
            due_date=date(2026, 3, 31),
            paid_date=None,
            status="Pending",
            description="Site assessment and permit filing",
            invoice_number="INV-2026-0018",
        ),
        # Additional paid payments
        Payment(
            property_id=p1.id,
            contractor_id=c1.id,
            amount=18000,
            due_date=date(2025, 10, 1),
            paid_date=date(2025, 10, 3),
            status="Paid",
            description="Demolition and site prep",
            invoice_number="INV-2025-0038",
        ),
        Payment(
            property_id=p2.id,
            contractor_id=c6.id,
            amount=24000,
            due_date=date(2026, 2, 1),
            paid_date=date(2026, 2, 5),
            status="Paid",
            description="Demolition Phase 1",
            invoice_number="INV-2026-0005",
        ),
    ]
    db.add_all(payments)
    db.commit()
    print(
        f"Database seeded: {len([p1, p2, p3, p4])} properties, "
        f"8 contractors, {len(schedules)} schedules, "
        f"{len(payments)} payments"
    )
