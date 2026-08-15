# Task 8: Accessibility Analyzer

## Objective

Integrate accessibility scanning to detect common WCAG issues and surface actionable findings.

## Description

Use automated accessibility libraries to scan rendered pages for missing alt attributes, missing labels, ARIA violations, color contrast problems, and other programmatically detectable issues. Normalize findings to Issue format and include element selectors.

## Files and Folders

```
backend/
├── app/
│   ├── analyzers/
│   │   └── accessibility_analyzer.py
│   └── crawler/
│       └── page_worker.py
docs/
└── docs/task-08-accessibility-analyzer.md
```

## Tools Used

* axe-core (via playwright-axe or injecting axe.min.js)
* Playwright

## Implementation Steps

1. Add axe-core injection in page_worker after page load.
2. Run axe analysis and collect results.
3. Convert axe results into the Issue schema with element selectors and recommendations.
4. Persist to DB and tag with WCAG IDs where available.
5. Add QA tests and sample failing pages.

## Expected Output

Automated accessibility findings persisted as Issues with actionable guidance.

## Dependencies

Depends on Task 5 (crawler) and Task 3 (DB).

