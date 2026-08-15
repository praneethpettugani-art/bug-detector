# Task 4: Scan Job Queue

## Objective

Implement background job processing using Redis and BullMQ equivalent for Python (RQ, Dramatiq, or Celery) to handle scan orchestration asynchronously.

## Description

When the API receives a scan request it should create a scan job record and enqueue a background worker job. Workers will process crawler orchestration and analyzers. Job state and progress updates must be persisted.

## Files and Folders

```
backend/
├── app/
│   ├── workers/
│   │   ├── worker.py
│   │   └── jobs.py
│   ├── services/
│   │   └── queue_service.py
└── requirements.txt
```

## Tools Used

* Redis
* RQ or Celery (recommend: Celery with Redis broker or Dramatiq)
* Python

## Implementation Steps

1. Choose worker framework (Celery recommended) and add to requirements.
2. Implement queue_service.enqueue_scan(scanId, payload).
3. Create worker that consumes scan jobs and runs orchestrator pipeline.
4. Add job status tracking in DB (pending, running, completed, failed).
5. Implement retry and error handling policy.
6. Add local Docker Compose config for Redis and worker.

## Expected Output

API enqueues jobs; workers pick up jobs and update scan status. Scan jobs are processed asynchronously and can be retried.

## Dependencies

Depends on Task 2 (scan endpoint) and Task 3 (DB schema).

