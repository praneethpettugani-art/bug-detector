# Task 22: CI/CD

## Objective

Create GitHub Actions workflows for tests, linting, and build to enforce quality on PRs.

## Description

Implement workflows to install dependencies, run linters, run tests, and build artifacts for frontend and backend. Optionally add deployment job for main branch.

## Files and Folders

```
.github/workflows/
├── ci.yml
└── deploy.yml
docs/
└── docs/task-22-ci-cd.md
```

## Tools Used

* GitHub Actions
* Actions for Python, Node, Docker

## Implementation Steps

1. Add ci.yml that sets up Python and Node, installs deps, runs linters and tests.
2. Add caching for dependency managers.
3. Optionally add deploy.yml to push Docker images or deploy to cloud.
4. Document workflow triggers and required secrets.

## Expected Output

CI runs on PRs and prevents regressions.

## Dependencies

Depends on Task 20 (tests) and Tasks 13/2 (projects to build).

