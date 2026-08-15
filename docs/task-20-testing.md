# Task 20: Testing

## Objective

Define testing strategy and add tests for backend, crawler, analyzers, DB, and key frontend components.

## Description

Create unit, integration, and end-to-end tests to validate critical paths: enqueueing scans, worker processing, crawler behavior, analyzers, and API contracts. Setup test DB and CI test runs.

## Files and Folders

```
backend/
├── tests/
│   ├── unit/
│   └── integration/
frontend/
├── tests/
│   └── e2e/
docs/
└── docs/task-20-testing.md
```

## Tools Used

* Pytest
* Playwright test (for e2e)
* Supertest or testing-library for frontend
* FactoryBoy / fixtures

## Implementation Steps

1. Add pytest configuration and sample unit tests for services.
2. Add integration tests that use a test Postgres and Redis (Docker compose test profile).
3. Add Playwright e2e tests that simulate scans against a controlled site.
4. Add frontend unit tests for key components.
5. Integrate tests into GitHub Actions.

## Expected Output

Test suite covering critical functionality and executed in CI on PRs.

## Dependencies

Depends on many earlier tasks (2, 3, 4, 5, 6–11, 13).

