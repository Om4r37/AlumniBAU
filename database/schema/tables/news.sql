CREATE TABLE news (
    id INTEGER PRIMARY KEY,
    thumbnail BLOB,
    archived BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id) REFERENCES posts(id)
);