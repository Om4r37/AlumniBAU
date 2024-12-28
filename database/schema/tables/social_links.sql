CREATE TABLE social_links (
    id INTEGER PRIMARY KEY,
    alumni_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    link TEXT NOT NULL,
    FOREIGN KEY (alumni_id) REFERENCES alumni(id)
);