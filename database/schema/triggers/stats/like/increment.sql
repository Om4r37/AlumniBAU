CREATE TRIGGER like_stats_increment AFTER INSERT ON likes BEGIN
    UPDATE stats SET likes_count = likes_count + 1;
    UPDATE posts SET likes_count = likes_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET likes_count = likes_count + 1 WHERE id = NEW.user_id;
END;