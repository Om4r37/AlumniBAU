CREATE TABLE alumni_posts (
    id INTEGER PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES posts(id)
);