Title: Implement events calendar and certificate issuance

Description:
Provide a first-class `Event` model and workflow for creating events, sharing them with groups, and issuing certificates to participants.

Acceptance criteria:
- `Event` model with name, start/end, all-day flag, details, and shared groups.
- Ability to list events and view event details via API.
- Certificate issuance endpoint that records participant name, event, and issue date.

Notes:
- Consider integrating a simple calendar view in the frontend.
- Include ability for event admins to add/remove participants.

Priority: Medium
