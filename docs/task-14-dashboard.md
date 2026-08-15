# Task 14: Dashboard

## Objective

Create a dashboard showing scan summaries and key metrics (health score, pages scanned, issue counts by severity).

## Description

Dashboard aggregates results from the Issues and Scans endpoints. Display cards for counts, charts, and quick links to issues and sitemap.

## Files and Folders

```
frontend/
├── src/
│   ├── pages/
│   │   └── Dashboard.tsx
│   └── components/
│       └── MetricCard.tsx
docs/
└── docs/task-14-dashboard.md
```

## Tools Used

* React
* Charting library (Recharts or Chart.js)

## Implementation Steps

1. Create Dashboard page that fetches scan summary from API.
2. Implement MetricCard and charts for issue distribution.
3. Add health score computation and visualization.
4. Ensure responsiveness and accessibility.

## Expected Output

Dashboard displays metrics for completed scans and links to drill-down views.

## Dependencies

Depends on Tasks 2, 11, and 13.

