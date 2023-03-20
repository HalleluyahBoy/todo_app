CREATE TABLE reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    reminder TEXT,
    date_time TEXT,
    created_at TEXT,
    updated_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
