# Task 16: Issue and Error Panels

## Objective

Provide frontend screens to browse, filter, search, and inspect detected issues.

## Description

Issue list UI supports filters (severity, category, page), search, sorting, and expandable item details showing DOM element, stack trace or code snippet, and suggested fixes.

## Files and Folders

```
frontend/
├── src/
│   ├── pages/
│   │   └── IssuesPage.tsx
│   └── components/
│       └── IssueList.tsx
docs/
└── docs/task-16-issue-and-error-panels.md
```

## Tools Used

* React
* TypeScript
* UI library (Chakra UI or Material UI)

## Implementation Steps

1. Implement IssuesPage calling API to list issues with pagination.
2. Build filter controls and search.
3. Render IssueList with expandable details and copy-to-clipboard for selectors.
4. Add link to open the page in the sitemap and highlight node.

## Expected Output

Users can browse and triage issues, filter by severity, and view details and recommendations.

## Dependencies

Depends on Tasks 11, 13, and 14.

