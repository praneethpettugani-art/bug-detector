# Task 6: Broken Link Analyzer

## Objective

Implement analyzer to validate discovered links, detect 4xx/5xx responses and problematic redirects, and record issues.

## Description

Analyzer will iterate over page resource and anchor links discovered by the crawler and perform HTTP HEAD/GET checks with follow-redirect policies and timeout. It should detect 404, 500, redirect loops, and mixed content issues.

## Files and Folders

```
backend/
├── app/
│   ├── analyzers/
│   │   └── broken_link_analyzer.py
│   └── services/
│       └── http_client.py
docs/
└── docs/task-06-broken-link-analyzer.md
```

## Tools Used

* Requests or httpx (async)
* Retry/backoff utilities

## Implementation Steps

1. Implement http_client with async support, timeouts, and redirect controls.
2. Implement broken_link_analyzer which takes discovered links and checks status codes.
3. Map results to unified Issue format and persist.
4. Add rate limiting and concurrency controls.
5. Add unit tests and integration tests with test pages.

## Expected Output

Detected broken links associated with pages stored as Issues in DB with severity mapping.

## Dependencies

Depends on Task 5 (crawler) and Task 3 (DB models).

