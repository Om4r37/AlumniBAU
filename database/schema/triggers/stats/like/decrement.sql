CREATE TRIGGER like_stats_decrement BEFORE DELETE ON likes BEGIN
    UPDATE stats SET likes_count = likes_count - 1;
    UPDATE posts SET likes_count = likes_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET likes_count = likes_count - 1 WHERE id = OLD.user_id;
END;