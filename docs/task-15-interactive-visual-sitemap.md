# Task 15: Interactive Visual Sitemap

## Objective

Implement an interactive 2D sitemap visualization showing pages as nodes and relationships.

## Description

Render sitemap using a client-side graph library with pan, zoom, node click, and severity-based node coloring. Clicking a node shows page details and issues.

## Files and Folders

```
frontend/
├── src/
│   ├── components/
│   │   └── SitemapGraph.tsx
docs/
└── docs/task-15-interactive-visual-sitemap.md
```

## Tools Used

* React
* visx, D3, or Cytoscape.js (recommend Cytoscape.js or vis-network)

## Implementation Steps

1. Choose and install graph library (Cytoscape.js recommended).
2. Implement SitemapGraph component that renders nodes and edges from API sitemap output.
3. Add pan/zoom, node tooltips, and click handlers to open page detail modal.
4. Color nodes by highest severity on the page.
5. Performance-tune for large sitemaps with clustering.

## Expected Output

Interactive sitemap component embedded in dashboard with node interactions.

## Dependencies

Depends on Task 5 (crawler producing sitemap), Task 11 (issue aggregator), and Task 13 (frontend setup).

