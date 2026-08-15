# Task 17: Historical Analytics

## Objective

Implement scan history and trend charts to show site health evolution over time.

## Description

Persist scan summaries per run and provide endpoints and frontend charts for trends (health score, issue counts by severity) over 30/90 days.

## Files and Folders

```
backend/
├── app/
│   └── api/
│       └── analytics_routes.py
frontend/
├── src/
│   └── pages/
│       └── AnalyticsPage.tsx
docs/
└── docs/task-17-historical-analytics.md
```

## Tools Used

* Postgres time-series queries
* Charting library (Recharts)

## Implementation Steps

1. Add ScanHistory table to DB (if separate) or ensure Scan rows include summary stats.
2. Implement analytics API endpoints returning time-series data.
3. Create frontend charts for 30-day, 90-day trends with interactive tooltips.
4. Add caching for expensive queries.

## Expected Output

Users can view historical trends and download snapshots.

## Dependencies

Depends on Tasks 3, 11, 13, and 14.

