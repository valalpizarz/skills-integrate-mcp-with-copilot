Title: Add attendance subsystem with Wi‑Fi Module integration

Description:
Create an attendance subsystem that can accept logs from a Wi‑Fi-based attendance module (e.g., Raspberry Pi). Track `lastSeen`, `duration`, and sessions per member.

Acceptance criteria:
- `Module` model to represent an attendance device (SSID, seed, refresh interval).
- `Log` model for member presence with date, lastSeen, duration, sessions JSON.
- API endpoint to accept attendance logs from the module (securely).

Notes:
- Start with a simple POST API that validates an API token.
- Add aggregation endpoints: member presence, average duration.

Priority: Medium
