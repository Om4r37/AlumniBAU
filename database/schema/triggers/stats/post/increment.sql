CREATE TRIGGER post_stats_increment AFTER INSERT ON posts BEGIN
    UPDATE stats SET posts_count = posts_count + 1;
    UPDATE users SET posts_count = posts_count + 1 WHERE id = NEW.user_id;
END;