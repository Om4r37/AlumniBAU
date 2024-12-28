CREATE TRIGGER comment_stats_increment AFTER INSERT ON comments BEGIN
    UPDATE stats SET comments_count = comments_count + 1;
    UPDATE posts SET comments_count = comments_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET comments_count = comments_count + 1 WHERE id = NEW.user_id;
END;