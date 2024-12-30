CREATE TABLE news (
    id INTEGER PRIMARY KEY,
    thumbnail BLOB,
    FOREIGN KEY (id) REFERENCES posts(id)
);