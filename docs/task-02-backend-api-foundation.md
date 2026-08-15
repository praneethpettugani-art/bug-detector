# Task 2: Backend API Foundation

## Objective

Create a scalable backend API foundation that accepts scan requests and serves results to the frontend.

## Description

Implement a FastAPI (Python) backend with modular structure: API routes, services, models (DB-agnostic), and configuration. Provide health endpoints and a basic /scan endpoint that accepts a URL and returns a scanId.

## Files and Folders

```
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   └── scan_service.py
│   ├── core/
│   │   └── config.py
│   └── db/
│       └── connection.py
└── requirements.txt
```

## Tools Used

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic
* SQLAlchemy (or async equivalent)
* Alembic (migrations)

## Implementation Steps

1. Create a new backend app using FastAPI and Uvicorn.
2. Implement configuration loading (env & .env) in core/config.py.
3. Add a simple DB connection wrapper in db/connection.py.
4. Add routes: health, /scan (POST) which validates input and enqueues a job.
5. Add scan_service.scan_request() that creates a scan record and returns scanId.
6. Document API in docs/api/api-documentation.md (placeholder).

## Expected Output

Running backend will expose health and /scan endpoints. A POST /scan returns a persistent scanId and stores initial scan job metadata.

## Dependencies

Depends on Task 1 (folder structure and env examples).

