CREATE TRIGGER comment_stats_decrement BEFORE DELETE ON comments BEGIN
    UPDATE stats SET comments_count = comments_count - 1;
    UPDATE posts SET comments_count = comments_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET comments_count = comments_count - 1 WHERE id = OLD.user_id;
END;