# Task 5: Website Crawler

## Objective

Implement a robust crawler using Playwright to visit pages, discover internal links, and collect DOM, network, and console data.

## Description

Crawler orchestrator should accept a start URL, normalize and restrict to same origin or configured scope, visit pages (breadth-first or prioritized), extract links, resources, HTTP status, DOM snapshots, performance timings, and console logs. It should handle dynamic JavaScript content with waits and timeouts.

## Files and Folders

```
backend/
├── app/
│   ├── crawler/
│   │   ├── crawler.py
│   │   └── page_worker.py
│   └── services/
│       └── sitemap_builder.py
docs/
└── docs/task-05-website-crawler.md
```

## Tools Used

* Playwright (Python)
* Async Python (asyncio)
* URL-normalization libraries (yarl, furl)

## Implementation Steps

1. Add Playwright to backend dependencies and setup Playwright install step.
2. Implement crawler.crawler that manages queue of URLs, deduplication, and concurrency limits.
3. Implement page_worker to visit a URL, wait for network idle or timeout, capture DOM, response status, resource timing, and console messages.
4. Persist page records in DB and push data to analyzers.
5. Ensure robots.txt respect (configurable), scope controls, rate limits, and user-agent header.
6. Add tests using a small local test site.

## Expected Output

Crawler that can visit a URL, discover internal pages, capture DOM and console logs, and store per-page metadata. Sitemap tree available.

## Dependencies

Depends on Task 4 (job queue) and Task 3 (DB to store pages).

