# Project Charter: contractor-scheduling-tracker

## Problem Statement

Reinhard von Hollander manages multiple real estate redevelopment projects simultaneously — buying properties, demolishing existing structures, rebuilding higher quality homes, and reselling. Tracking which contractors are scheduled where, what has been paid versus what is owed, and how actual spend compares to budget currently happens across disconnected spreadsheets and email threads.

**Who is affected:** Real estate developer (Reinhard), project managers, accounting staff.

**Current state:** Manual spreadsheet tracking with no unified view across properties.

## Solution Overview

A web-based tracker providing a single dashboard for all active redevelopment projects, with dedicated views for contractor scheduling, payment status, and budget tracking per property. This is initially a demo to demonstrate the concept — all data is fictional and pre-seeded.

## Scope

### In Scope (v1)

- [x] Dashboard with summary cards (active projects, total budget, payments due, overdue alerts)
- [x] Property tracker with stage pipeline (Purchased → Demolition → Rebuild → Listed → Sold)
- [x] Contractor directory with trade specializations, rates, and assignment history
- [x] Schedule view showing contractor assignments per property with date ranges
- [x] Payment tracker with status filtering (Pending, Paid, Overdue)
- [x] Pre-seeded realistic demo data (4 properties, 8 contractors, 22 payment records)
- [x] Online deployment (Railway)

### Out of Scope (v1)

- User authentication and role-based access (demo only)
- Document/file attachments (permits, contracts, invoices)
- Mobile app (responsive web only)
- Integration with QuickBooks or accounting software
- Real-time notifications or email alerts
- Multi-user concurrent editing
- CRUD operations (create/edit/delete records via the UI)

## Users & Personas

| Persona | Role | Primary Need | Interaction Model |
|---|---|---|---|
| Reinhard von Hollander | Real estate developer / owner | See portfolio status at a glance; know who is working where and what is owed | Web dashboard, daily check-in |
| Project Manager | Property site coordinator | Track contractor schedules and flag overdue payments | Properties and Schedule views |
| Accountant | Financial oversight | Verify payment status and compare budget to actuals | Payments and Properties detail views |

## Success Metrics

| Metric | Target | How Measured |
|---|---|---|
| Demo impressiveness | Reinhard can navigate the full app in under 5 minutes without explanation | Walkthrough during client meeting |
| Visual polish | Looks like a real production tool, not a prototype | Subjective review before demo |
| Customizability | Any label, property, or contractor can be updated in under 30 minutes | Developer review of seed data structure |

## Constraints & Assumptions

**Constraints:**
- Free-tier hosting only (Railway hobby plan)
- All data is fictional — no real PII or financial data
- No budget for external databases or paid services

**Assumptions:**
- Reinhard will review the demo and provide real requirements afterward
- A single developer (Cole) will maintain and customize the codebase
- SQLite is sufficient for a single-user demo; PostgreSQL upgrade path documented

## Timeline

| Milestone | Target | Deliverables |
|---|---|---|
| Project Setup | Day 1 | Folder structure, dependencies, CI pipeline |
| Data Model + Seed | Day 1-2 | SQLAlchemy models, 22 realistic payment records |
| Routes + Templates | Day 2-3 | All 6 pages rendering with seed data |
| Polish + Deploy | Day 3-4 | Custom CSS, Railway deployment, live URL |
