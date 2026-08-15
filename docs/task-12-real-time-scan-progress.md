# Task 12: Real-Time Scan Progress

## Objective

Provide real-time scan progress updates to the frontend via WebSocket or SSE.

## Description

Implement a publish/subscribe mechanism where workers emit progress events and API relays them to connected frontend clients. Events include lifecycle stages and counts.

## Files and Folders

```
backend/
├── app/
│   ├── api/
│   │   └── ws.py
│   ├── services/
│   │   └── progress_publisher.py
docs/
└── docs/task-12-real-time-scan-progress.md
```

## Tools Used

* WebSockets (via FastAPI WebSocket or Socket.IO)
* Redis Pub/Sub for cross-process propagation

## Implementation Steps

1. Add WebSocket endpoint and basic client authentication (scanId subscription).
2. Implement progress_publisher used by workers to publish events to Redis channel.
3. WebSocket handler subscribes to Redis and forwards messages to connected clients.
4. Ensure graceful reconnect and authentication.
5. Add tests for message flow.

## Expected Output

Frontend can subscribe to scan events and display real-time progress updates.

## Dependencies

Depends on Task 4 (workers) and Task 2 (API).

