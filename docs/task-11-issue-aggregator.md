# Task 11: Issue Aggregator

## Objective

Unify analyzer outputs into a consistent Issue schema and provide services to query, deduplicate, and score issues.

## Description

Create a centralized aggregator that accepts analyze results, normalizes fields, deduplicates similar issues, and computes severity and impact for each site.

## Files and Folders

```
backend/
├── app/
│   ├── services/
│   │   └── issue_aggregator.py
│   └── db/
│       └── models.py (Issue model)
docs/
└── docs/task-11-issue-aggregator.md
```

## Tools Used

* Python
* DB (Postgres)

## Implementation Steps

1. Define canonical Issue schema and severity mapping.
2. Implement aggregator service to accept analyzer outputs and normalize them.
3. Implement deduplication heuristics (same selector, same error message, same resource URL).
4. Persist canonical Issues to DB and update scan-level summaries.
5. Provide API endpoints to query issues by severity, page, and category.

## Expected Output

All analyzer outputs consolidated into the Issues table and accessible through API.

## Dependencies

Depends on Tasks 3, 6–10 (analyzers) and Task 2 (API).

