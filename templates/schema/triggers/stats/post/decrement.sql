CREATE TRIGGER post_stats_decrement BEFORE DELETE ON posts BEGIN
    UPDATE stats SET posts_count = posts_count - 1;
    UPDATE users SET posts_count = posts_count - 1 WHERE id = OLD.user_id;
END;