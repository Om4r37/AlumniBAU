CREATE TRIGGER news_stats_increment AFTER INSERT ON news BEGIN
    UPDATE stats SET news_count = news_count + 1;
    UPDATE admins SET news_count = news_count + 1 WHERE id = (SELECT user_id FROM posts WHERE id = NEW.id);
END;