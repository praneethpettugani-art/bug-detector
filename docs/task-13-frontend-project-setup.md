# Task 13: Frontend Project Setup

## Objective

Initialize the frontend application and basic layout for the dashboard and scan form.

## Description

Create a React + TypeScript project with component scaffolding for URL input, scan config, scan button, and progress view. Establish API client and WebSocket connection utilities.

## Files and Folders

```
frontend/
├── package.json
├── src/
│   ├── App.tsx
│   ├── pages/
│   │   └── ScanPage.tsx
│   ├── components/
│   │   └── ScanForm.tsx
│   └── services/
│       └── api.ts
docs/
└── docs/task-13-frontend-project-setup.md
```

## Tools Used

* React
* TypeScript
* Vite or Create React App
* TailwindCSS or Chakra UI

## Implementation Steps

1. Scaffold project with Vite + React + TypeScript.
2. Add UI framework and linting (ESLint, Prettier).
3. Implement ScanForm component to POST to /scan.
4. Implement API client and wiring for WebSocket progress updates.
5. Document frontend setup in docs.

## Expected Output

Local frontend runs with a page to submit scan requests and receive progress updates.

## Dependencies

Depends on Task 2 (API) and Task 12 (real-time progress) for end-to-end behavior.

