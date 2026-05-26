Title: Status threads, daily logs and Telegram/Discord integration

Description:
Implement threaded status updates, daily logs of who posted, and integration to post summaries to Telegram and Discord groups.

Acceptance criteria:
- `Thread` model to define generation/due/log times and notification flags.
- `Message` and `DailyLog` models to record updates and summary lists (late, didNotSend).
- Integration adapters to send messages to Telegram/Discord (configurable tokens).

Notes:
- Start with Telegram only if time is limited; abstract platform adapters for later additions.
- Ensure secure storage of bot tokens (environment or secret store).

Priority: Medium
