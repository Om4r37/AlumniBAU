CREATE TABLE admins (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    manage BOOLEAN DEFAULT FALSE,
    announce BOOLEAN DEFAULT FALSE,
    stats BOOLEAN DEFAULT FALSE,
    mod BOOLEAN DEFAULT FALSE,
    news_count INTEGER DEFAULT 0,
    FOREIGN KEY (id) REFERENCES users(id)
);