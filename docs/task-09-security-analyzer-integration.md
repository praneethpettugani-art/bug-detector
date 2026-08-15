# Task 9: Security Analyzer Integration

## Objective

Integrate the existing static-security-analyzer module so security findings are included in scan results.

## Description

Call into static-security-analyzer after page DOM capture (or on downloaded assets) and ingest its findings into the Issue Aggregator. Keep the module separate and focused on security-specific checks (headers, TLS, insecure scripts, CSP issues, unsafe inline JS, secrets in source, etc.).

## Files and Folders

```
static-security-analyzer/
├── (existing module files)
backend/
├── app/
│   └── analyzers/
│       └── security_integration.py
docs/
└── docs/task-09-security-analyzer-integration.md
```

## Tools Used

* The repository's static-security-analyzer (Python)
* Standard security libraries

## Implementation Steps

1. Inspect static-security-analyzer interface and identify expected inputs/outputs.
2. Add an adapter (security_integration.py) that normalizes its output to the Issue schema.
3. Invoke security analysis for each page or asset as configured.
4. Ensure no unrelated frontend code is included in this module.
5. Add tests and example reports.

## Expected Output

Security findings from the static-security-analyzer appear as Issues alongside other analyzer results.

## Dependencies

Depends on Task 5 (crawler) and Task 3 (DB). Also requires the static-security-analyzer code present in repo.

