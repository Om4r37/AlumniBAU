CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    display_name TEXT DEFAULT 'Anonymous',
    phone_number TEXT,
    email TEXT,
    profile_picture BLOB,
    following_count INTEGER DEFAULT 0,
    followers_count INTEGER DEFAULT 0,
    posts_count INTEGER DEFAULT 0,
    comments_count INTEGER DEFAULT 0,
    likes_count INTEGER DEFAULT 0,
    dislikes_count INTEGER DEFAULT 0
);