# Task 7: JavaScript Error Analyzer

## Objective

Capture and analyze browser console errors, runtime exceptions, failed resource loads, and unhandled promises to surface JavaScript issues.

## Description

During page visits the crawler collects console messages and exceptions. This analyzer will normalize those logs, correlate them with page URLs and resource URLs, classify issue types (syntax error, runtime error, CSP violations), and persist Issues.

## Files and Folders

```
backend/
├── app/
│   ├── analyzers/
│   │   └── js_error_analyzer.py
│   └── crawler/
│       └── page_worker.py (emit console logs)
docs/
└── docs/task-07-javascript-error-analyzer.md
```

## Tools Used

* Playwright console capture
* Structured log normalization

## Implementation Steps

1. Ensure crawler captures console messages, stack traces, and resource failure events.
2. Implement js_error_analyzer to parse and classify errors.
3. Map to Issue schema with suggested remediation when possible.
4. Add tests using controlled pages that throw errors.

## Expected Output

JS runtime and console issues stored as Issues with stack traces and resource context.

## Dependencies

Depends on Task 5 (crawler) and Task 3 (DB).

