Title: Add groups, mentor/mentee relationships, and responsibilities

Description:
Add support for organizing members into groups, defining group admins, mentor/mentee relationships, and assigning responsibilities. Each group should allow toggles for attendance tracking and status updates.

Acceptance criteria:
- `Group` model with `admins`, `members`, and fields to enable attendance and status tracking.
- Mentor groups model linking mentors to mentees and options to send periodic reports.
- API endpoints to create/manage groups and assign roles (admin-only actions).

Notes / Implementation hints:
- Use many-to-many relationships for members/admins.
- Add group-level settings in the admin UI or protected endpoints.

Priority: High
