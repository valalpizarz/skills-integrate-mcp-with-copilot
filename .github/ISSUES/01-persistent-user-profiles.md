Title: Add persistent user profiles and member model

Description:
Implement persistent user profiles (database-backed) so students and club members have full profiles instead of in-memory emails. Profiles should include:
- Basic info: first/last name, email, phone, display name
- Social links: GitHub, GitLab, Telegram, Twitter
- Profile picture and cover image (upload support)
- Resume upload
- Interests, expertise, languages

Acceptance criteria:
- A database-backed `User` and `Profile` model exists and is persisted using the project's chosen ORM.
- API endpoints to get and update profiles (authenticated) are available.
- Static files (profile pictures, resumes) are uploaded to a configurable storage path.

Notes / Implementation hints:
- For FastAPI, reuse SQLModel/SQLAlchemy and Pydantic schemas.
- Add endpoints: `GET /users/{email}`, `PUT /users/{email}` (auth required).
- Add migration guidance in README.

Priority: High
