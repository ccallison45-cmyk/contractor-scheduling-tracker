# Contractor Scheduling & Payment Tracker — User Guide

Welcome to your Contractor Scheduling & Payment Tracker. This guide walks you through every page of the app and what you can do on each one.

---

## Getting Started

Open the app in any web browser using the link provided. No login is required — the app opens straight to the Dashboard.

The **navigation bar** at the top of every page has five sections:

| Button | What it shows |
|---|---|
| **Dashboard** | Big-picture summary of your entire portfolio |
| **Properties** | All your properties and their current stage |
| **Contractors** | Your contractor directory |
| **Schedule** | Who is working where and when |
| **Payments** | Every payment — paid, pending, and overdue |

---

## Dashboard

This is your home screen — a snapshot of everything happening across all your properties.

**Top cards** show at-a-glance numbers:
- **Active Projects** — How many properties are currently in progress (not yet sold)
- **Total Paid** — Total dollars paid to contractors across all properties
- **Due This Month** — How many payments are due this calendar month and their total dollar amount
- **Overdue** — Payments that are past due (shown in red if any exist)

**Properties table** (left side) shows every property with:
- The street address
- Current stage (color-coded badge)
- Total budget and amount spent
- A progress bar showing how much of the budget has been used
  - Green = under 80% used
  - Yellow = 80-95% used
  - Red = over 95% used

Click any property row to jump to its detail page.

**Recent Payments** (right side) shows the last 5 payments with contractor name, amount, and status.

---

## Properties

### Property List

Shows all your properties as cards. Each card displays:
- Street address and city
- Current stage badge (Purchased, Demolition, Rebuild, Listed, or Sold)
- Budget usage bar
- Number of contractors currently working on-site
- Purchase date and price

**Filter tabs** at the top let you view:
- **All** — Every property
- **Active** — Properties still in progress (not Listed or Sold)
- **Completed** — Properties that are Listed or Sold

Click **View Details** on any card to see the full property breakdown.

### Property Detail

Everything about one property in one place.

**Header section** shows:
- Full address and current stage
- Notes about the property
- Four key numbers: Purchase Price, Total Budget, Amount Spent, Remaining Budget

**Stage pipeline** — A visual indicator showing where the property is in the process:

```
Purchased → Demolition → Rebuild → Listed → Sold
```

Completed stages show green checkmarks. The current stage is highlighted in blue.

**Two tabs below:**

- **Contractors & Schedule** — Every contractor assigned to this property, their trade, what work they're doing, the date range, and whether the work is Scheduled, In Progress, or Completed. Click a contractor name to see their full profile.

- **Payments** — Every payment for this property. Shows description, contractor, invoice number, amount, due date, and status. Color-coded rows:
  - Green = Paid
  - Red = Overdue
  - Totals are shown at the bottom (Paid, Pending, Overdue)

---

## Contractors

### Contractor List

A searchable directory of all your contractors.

**Search bar** at the top — type any name, trade, or keyword to filter the list instantly.

The table shows:
- Company name
- Contact person and phone number
- Trade specialty (color-coded badge)
- Hourly rate (or "Fixed bid" for contractors who quote per job)
- Number of active jobs they're currently working
- Total amount paid to them to date

Click any row to see the contractor's full profile.

### Contractor Detail

Full profile for one contractor.

**Profile card** shows:
- Company name and trade
- Contact person, phone, and email
- Rate information
- Total paid to date (all-time, across all properties)

**Two tabs below:**

- **Assignments** — Every property this contractor has been assigned to, with scope of work, dates, and status. Click a property name to jump to that property's detail page.

- **Payment History** — Every payment made (or pending) to this contractor across all properties. Shows property, description, invoice number, amount, due date, and status. Total paid shown at the bottom.

---

## Schedule

Shows **who is working where and when** — organized by property.

Each property appears as a section with its address and current stage. Inside each section, every contractor assignment is shown as a card with:
- Contractor name (clickable to view their profile)
- Trade badge
- What work they're doing (scope)
- Start and end dates
- Status badge (Scheduled, In Progress, Completed)

**Active only toggle** (top right) — Switch this on to hide completed and cancelled assignments, showing only current and upcoming work.

Cards are color-coded on the left edge:
- Blue = In Progress
- Light blue = Scheduled (upcoming)
- Green = Completed
- Gray = Cancelled

---

## Payments

The complete payment ledger across all properties and contractors.

**Summary cards** at the top show three totals:
- Total Paid (green)
- Total Pending (yellow)
- Total Overdue (red)

**Filter controls** let you narrow down the list:
- **Property dropdown** — Show payments for one specific property
- **Contractor dropdown** — Show payments to one specific contractor
- **Status dropdown** — Show only Paid, Pending, or Overdue
- **Clear Filters** button resets all filters

**Payment table** shows every payment with:
- Due date (and paid date if applicable)
- Property address (clickable)
- Contractor name (clickable)
- Description of work
- Invoice number
- Amount
- Status badge

Row colors:
- Green background = Paid
- Red background = Overdue
- No background = Pending

---

## Understanding the Stages

Each property moves through these stages during redevelopment:

| Stage | What it means |
|---|---|
| **Purchased** | Property has been acquired. Planning and permits in progress. |
| **Demolition** | Existing structure is being torn down or stripped. |
| **Rebuild** | New construction or renovation is underway. |
| **Listed** | Work is complete. Property is on the market for sale. |
| **Sold** | Property has been sold. Project is closed out. |

---

## Understanding Payment Statuses

| Status | What it means |
|---|---|
| **Paid** (green) | Invoice has been paid. Shows the date it was paid. |
| **Pending** (yellow) | Invoice received but not yet paid. Due date is in the future. |
| **Overdue** (red) | Invoice is past its due date and has not been paid. Needs attention. |

---

## Quick Reference

| I want to... | Where to go |
|---|---|
| See the big picture | Dashboard |
| Check on a specific property | Properties → click the property |
| See who's working this week | Schedule (toggle "Active only") |
| Find out what I owe a contractor | Contractors → click the contractor → Payment History tab |
| See all overdue payments | Payments → filter by Status: Overdue |
| Check a property's budget | Properties → click the property → look at the header stats |
| Find a contractor's phone number | Contractors → click the contractor |

---

*This is a demo version with sample data. All property addresses, contractor names, and financial figures are fictional. Once you're ready, we'll customize it with your real information.*
