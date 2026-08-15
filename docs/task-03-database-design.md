# Task 3: Database Design

## Objective

Design and implement database schema/models for users, projects, scan jobs, pages, detected issues, severity, and historical scan results.

## Description

Create normalized schemas with relationships optimized for querying scan results, issues by severity, and historical trends. Use PostgreSQL as primary store.

## Files and Folders

```
backend/
├── app/
│   ├── db/
│   │   └── models.py
│   ├── migrations/
│   │   └── (alembic files)
docs/
└── docs/task-03-database-design.md
```

## Tools Used

* PostgreSQL
* SQLAlchemy (ORM) or async ORM (SQLModel/Databases)
* Alembic for migrations
* PgAdmin or DBeaver for exploration

## Implementation Steps

1. Define ER model: Users, Projects, Scans, Pages, Issues, Severities, ScanHistory.
2. Implement SQLAlchemy models in backend/app/db/models.py.
3. Add indices on scanId, pageUrl, createdAt, severity for performance.
4. Create Alembic migration scripts.
5. Document schema in docs (this file).

## Expected Output

A working database schema migrated to Postgres with tables and relationships. Backend models match DB schema.

## Dependencies

Depends on Task 2 (backend foundation) and Task 1 (repo prep).

