Title: Add admin UI and import/export support for bulk data

Description:
Provide an admin interface for managing users, groups, events, and projects. Add CSV import/export to onboard bulk user/project data.

Acceptance criteria:
- Basic admin UI (can be built with a simple protected React page or use Django admin if migrating) to CRUD core models.
- CSV import/export endpoints or tools to bulk upload users and projects.

Notes:
- If staying with FastAPI, consider `fastapi-admin` or a simple protected frontend + APIs.

Priority: Low
