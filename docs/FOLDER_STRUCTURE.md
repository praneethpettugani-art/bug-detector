# Proposed Folder Structure for bug-detector (Backend Engine)

This document proposes a clear folder layout for the backend-focused "bug-detector" repository (backend engine only). The UI/Visualizer should remain in a separate repository (bug-detector-ui) as requested.

Overview: Keep this repo focused on the scanning engine, analyzers, crawlers, data storage, and CI for backend logic. The frontend should be a dedicated repository that consumes the backend API.

Top-level layout

```
bug-detector/                       # backend engine repository (this repo)
├── backend/                         # main backend engine package
│   ├── api/                         # REST/GraphQL API handlers, websocket gateways
│   │   ├── server.py
│   │   └── routes/
│   ├── crawler/                     # web crawler / headless runner wrappers (Playwright/Puppeteer adapter)
│   │   ├── runner.py
│   │   └── discover.py
│   ├── engine/                      # scan orchestration, job scheduler, task workers
│   │   ├── orchestrator.py
│   │   └── worker.py
│   ├── analyzers/                   # modular analyzer plugins (python, c/c++, accessibility, etc.)
│   │   ├── python_analyzer.py
│   │   ├── c_cpp_analyzer.py
│   │   └── accessibility.py
│   ├── storage/                     # persistence layer adapters (Postgres, object storage clients)
│   │   ├── db.py
│   │   └── object_store.py
│   ├── queue/                       # queue clients / background job connectors (Redis / BullMQ wrappers)
│   │   └── redis_queue.py
│   └── utils/                       # shared helpers, logging, config
│       ├── logging.py
│       └── config.py
│
├── samples/                         # sample vulnerable files & test pages
├── scripts/                         # dev scripts (local runner, bootstrap, migrations)
├── tests/                           # unit & integration tests for backend
├── docs/                            # documentation (architecture, folder structure, API docs)
│   └── FOLDER_STRUCTURE.md          # this file
├── docker/                          # Docker deployment artifacts and k8s manifests
├── .github/                         # CI workflows and issue templates
├── requirements.txt                 # pinned Python dependencies (if any)
├── pyproject.toml or setup.py       # packaging/config (optional)
├── README.md                        # repository README (backend-focused summary)
└── LICENSE
```

Notes and rationale

- backend/: Keep all runtime engine code under a single package so import paths and packaging are straightforward.
- analyzers/: Each analyzer is a plugin-like module. Keep a stable plugin interface (e.g., analyze(path, config) -> findings) so new analyzers (JS linter, accessibility rules, network heuristics) can be added without changing orchestration logic.
- crawler/: The long-term plan calls for an asynchronous headless runner; the code in crawler/ should be a thin adapter that can run either Playwright, Puppeteer, or a custom headless runner. Keep the runner API consistent: discover(url) -> sitemap; fetch_page(url) -> page_payload.
- queue/: Provide adapters for queuing backends (Redis, RQ, Celery). The orchestrator/worker should be queue-agnostic and interact via a small abstraction.
- storage/: Use Postgres for relational records (scans, pages, findings) and an object store (S3-compatible) for snapshots and report artifacts.
- docs/: Keep architectural notes, API contracts (OpenAPI), and onboarding docs here.

Frontend (separate repo)

- Create a dedicated repository: `bug-detector-ui`
  - Purpose: Dashboard, interactive sitemap, exports, charts, and client-facing features.
  - Technology suggestions: React + Vite, react-flow (sitemap), Chart.js or Recharts for trends, Tailwind CSS or plain CSS.
  - This backend repo should expose REST endpoints and websocket progress updates the UI consumes.

Suggested API surface (examples)

- POST /scans { url, options } -> 201 { scan_id }
- GET /scans/:id/status -> { status, progress }
- GET /scans/:id/results -> { sitemap, findings }
- WS /scans/:id/progress -> real-time progress messages

Example development workflow

1. Implement a lightweight local runner in backend/engine/orchestrator.py that accepts simple scan requests and stores results in storage/
2. Add unit tests in tests/ that validate analyzer modules (use samples/ as fixtures)
3. Start a minimal API in backend/api/server.py to accept POST /scans and respond with a fake sitemap for early UI development
4. Create the `bug-detector-ui` repo (separate) and point its VITE_API_BASE to the backend API

What I added

- docs/FOLDER_STRUCTURE.md describing the recommended folder layout and next steps for separating UI into bug-detector-ui and keeping this repo backend-only.

Next steps I can take for you

- Create the `bug-detector-ui` starter repo and push the frontend scaffold (React + Vite) I prepared earlier.
- Open a branch in this repo and create the backend top-level folders and placeholder __init__.py files and basic module stubs (api/server.py, engine/orchestrator.py, analyzers/__init__.py, etc.) to make the structure importable and testable.
- Add a minimal local mock server (Flask/FastAPI) under backend/api for UI integration testing.

If you want me to proceed with creating the frontend repo or adding the stub files in this repo, tell me which action to take and I will commit the changes to a branch (I used `docs/folder-structure` for this doc).