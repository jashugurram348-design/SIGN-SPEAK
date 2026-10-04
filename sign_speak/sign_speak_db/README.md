# SignSpeak Database

This database module provides SQLite database functionality for the SignSpeak application.

It manages:

- Sign-language dictionary data
- Translation history
- Learning progress
- Database initialization
- Sign searching
- Sign categories

---

## Database Technology

SignSpeak uses:

- SQLite
- Python `sqlite3`
- Python `datetime`

SQLite is included with Python, so no additional database package is required.

---

## Database File

The database is automatically created as:

```text
signspeak.db