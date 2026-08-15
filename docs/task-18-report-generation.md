# Task 18: Report Generation

## Objective

Provide PDF and CSV report generation for scan results and allow shareable links.

## Description

Generate downloadable and shareable reports summarizing issues, pages, and metrics. Support PDF rendering (server-side) and CSV export for tabular data.

## Files and Folders

```
backend/
├── app/
│   ├── services/
│   │   └── report_service.py
│   └── api/
│       └── reports_routes.py
docs/
└── docs/task-18-report-generation.md
```

## Tools Used

* WeasyPrint, wkhtmltopdf, or Playwright PDF generation
* Pandas or csv module for CSV exports

## Implementation Steps

1. Implement report_service to assemble scan data into templates.
2. Use a PDF engine (WeasyPrint or Playwright) to render HTML to PDF.
3. Implement CSV export endpoint.
4. Add secure, time-limited shareable links (signed tokens).

## Expected Output

Users can download PDF/CSV reports and share scan summaries via links.

## Dependencies

Depends on Tasks 11 and 14.

