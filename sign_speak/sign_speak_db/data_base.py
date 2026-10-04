# database.py

import sqlite3
from pathlib import Path
from datetime import datetime

# Database location
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "signspeak.db"


def get_connection():
    """Create and return a database connection."""
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    """Create the database tables if they don't exist."""
    connection = get_connection()
    cursor = connection.cursor()

    # Signs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            description TEXT,
            image TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # Translation history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS translation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT NOT NULL,
            translated_text TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # Learning progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_name TEXT NOT NULL UNIQUE,
            completed INTEGER DEFAULT 0,
            completed_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_sign(name, category, description="", image=""):
    """Add a new sign to the database."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO signs
            (name, category, description, image, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            name,
            category,
            description,
            image,
            datetime.now().isoformat()
        ))

        connection.commit()

    except sqlite3.IntegrityError:
        # Sign already exists
        pass

    connection.close()


def get_all_signs():
    """Return all signs."""
    connection = get_connection()

    signs = connection.execute("""
        SELECT *
        FROM signs
        ORDER BY name
    """).fetchall()

    connection.close()

    return [dict(sign) for sign in signs]


def get_sign(name):
    """Return one sign by name."""
    connection = get_connection()

    sign = connection.execute("""
        SELECT *
        FROM signs
        WHERE LOWER(name) = LOWER(?)
    """, (name,)).fetchone()

    connection.close()

    return dict(sign) if sign else None


def search_signs(query):
    """Search signs by name or category."""
    connection = get_connection()

    signs = connection.execute("""
        SELECT *
        FROM signs
        WHERE name LIKE ?
           OR category LIKE ?
        ORDER BY name
    """, (
        f"%{query}%",
        f"%{query}%"
    )).fetchall()

    connection.close()

    return [dict(sign) for sign in signs]


def get_signs_by_category(category):
    """Return signs belonging to a category."""
    connection = get_connection()

    signs = connection.execute("""
        SELECT *
        FROM signs
        WHERE LOWER(category) = LOWER(?)
        ORDER BY name
    """, (category,)).fetchall()

    connection.close()

    return [dict(sign) for sign in signs]


def add_translation_history(input_text, translated_text):
    """Save a translation to history."""
    connection = get_connection()

    connection.execute("""
        INSERT INTO translation_history
        (input_text, translated_text, created_at)
        VALUES (?, ?, ?)
    """, (
        input_text,
        translated_text,
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()


def get_translation_history(limit=50):
    """Return recent translation history."""
    connection = get_connection()

    history = connection.execute("""
        SELECT *
        FROM translation_history
        ORDER BY id DESC
        LIMIT ?
    """, (limit,)).fetchall()

    connection.close()

    return [dict(item) for item in history]


def clear_translation_history():
    """Delete all translation history."""
    connection = get_connection()

    connection.execute("""
        DELETE FROM translation_history
    """)

    connection.commit()
    connection.close()


def set_lesson_progress(lesson_name, completed=True):
    """Create or update learning progress."""
    connection = get_connection()

    completed_value = 1 if completed else 0
    completed_at = datetime.now().isoformat() if completed else None

    connection.execute("""
        INSERT INTO learning_progress
        (lesson_name, completed, completed_at)
        VALUES (?, ?, ?)
        ON CONFLICT(lesson_name)
        DO UPDATE SET
            completed = excluded.completed,
            completed_at = excluded.completed_at
    """, (
        lesson_name,
        completed_value,
        completed_at
    ))

    connection.commit()
    connection.close()


def get_learning_progress():
    """Return all learning progress."""
    connection = get_connection()

    progress = connection.execute("""
        SELECT *
        FROM learning_progress
        ORDER BY id
    """).fetchall()

    connection.close()

    return [dict(item) for item in progress]


# Initialize database when this file is imported
init_database()


if __name__ == "__main__":
    print("SignSpeak database initialized successfully.")
    print(f"Database location: {DATABASE}")