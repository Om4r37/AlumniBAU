CREATE TABLE admins (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    manage BOOLEAN DEFAULT 0,
    announce BOOLEAN DEFAULT 0,
    stats BOOLEAN DEFAULT 0,
    mod BOOLEAN DEFAULT 0,
    news_count INTEGER DEFAULT 0,
    FOREIGN KEY (id) REFERENCES users(id)
);