CREATE TRIGGER add_admin AFTER INSERT ON admins BEGIN
    INSERT INTO users (id, display_name) VALUES (NEW.id, NEW.username);
END;