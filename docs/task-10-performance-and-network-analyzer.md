# Task 10: Performance and Network Analyzer

## Objective

Collect performance metrics and network health information for pages and resources.

## Description

Record page load timings, resource timings, slow resources, failed requests, time to first byte, and general performance budgets. Map findings to Issues where thresholds are exceeded.

## Files and Folders

```
backend/
├── app/
│   ├── analyzers/
│   │   └── performance_analyzer.py
│   └── crawler/
│       └── page_worker.py
docs/
└── docs/task-10-performance-and-network-analyzer.md
```

## Tools Used

* Playwright tracing and Performance APIs
* Lighthouse (optional, as a separate job)

## Implementation Steps

1. Capture performance timing, resource timings, and network events in page_worker.
2. Implement performance_analyzer to compute metrics and flag slow resources.
3. Persist metrics to DB and create issues for critical performance problems.
4. Optionally integrate Lighthouse for deeper audits (as a heavyweight job).

## Expected Output

Performance metrics stored and key problems presented as Issues and analytics.

## Dependencies

Depends on Task 5 (crawler) and Task 3 (DB).

