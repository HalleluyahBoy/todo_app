PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    reminder TEXT NOT NULL,
    date_time TEXT NOT NULL
);
