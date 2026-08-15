# Task 19: Authentication and Project Management

## Objective

Add optional user accounts, authentication, and project management for multiple websites per user.

## Description

Implement user registration / login (JWT or session), project entity linking multiple sites, and per-project scan history and permissions.

## Files and Folders

```
backend/
├── app/
│   ├── api/
│   │   └── auth_routes.py
│   └── db/
│       └── user_models.py
docs/
└── docs/task-19-authentication-and-project-management.md
```

## Tools Used

* FastAPI security
* OAuth or JWT (PyJWT)
* Optional: Auth library (Keycloak or Auth0)

## Implementation Steps

1. Implement user model, registration, login, password hashing, and session or JWT issuance.
2. Add Project model that owners can manage.
3. Enforce authorization on scan and project endpoints.
4. Add UI for login, project creation, and per-project scans.

## Expected Output

Multi-user support with secure authentication and project scoping.

## Dependencies

Depends on Tasks 2, 3, and 11.

