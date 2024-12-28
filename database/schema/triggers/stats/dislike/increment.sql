CREATE TRIGGER dislike_stats_increment AFTER INSERT ON dislikes BEGIN
    UPDATE stats SET dislikes_count = dislikes_count + 1;
    UPDATE posts SET dislikes_count = dislikes_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET dislikes_count = dislikes_count + 1 WHERE id = NEW.user_id;
END;