CREATE TRIGGER dislike_stats_decrement BEFORE DELETE ON dislikes BEGIN
    UPDATE stats SET dislikes_count = dislikes_count - 1;
    UPDATE posts SET dislikes_count = dislikes_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET dislikes_count = dislikes_count - 1 WHERE id = OLD.user_id;
END;