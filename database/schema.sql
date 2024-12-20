CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone_number TEXT,
    email TEXT,
    profile_picture BLOB,
    following_count INTEGER DEFAULT 0,
    followers_count INTEGER DEFAULT 0,
    posts_count INTEGER DEFAULT 0,
    comments_count INTEGER DEFAULT 0,
    likes_count INTEGER DEFAULT 0,
    dislikes_count INTEGER DEFAULT 0
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    manage BOOLEAN DEFAULT 0,
    announce BOOLEAN DEFAULT 0,
    stats BOOLEAN DEFAULT 0,
    mod BOOLEAN DEFAULT 0,
    news_count INTEGER DEFAULT 0,
    FOREIGN KEY (id) REFERENCES users(id)
);

CREATE UNIQUE INDEX admins_username_index ON admins (username);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    publish_date TEXT NOT NULL,
    comments_count INTEGER DEFAULT 0,
    likes_count INTEGER DEFAULT 0,
    dislikes_count INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE news (
    id INTEGER PRIMARY KEY,
    expire_date TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES posts(id)
);

CREATE TABLE alumni (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,

    -- constants
    student_id INTEGER NOT NULL UNIQUE,
    nno_hash TEXT NOT NULL,
    full_name TEXT,
    nationality TEXT,
    gender BOOLEAN,
    GPA INTEGER,
    major_id INTEGER,
    degree_id INTEGER,
    graduation_year INTEGER,
    graduation_semester INTEGER,

    -- variables
    phone_number TEXT,
    work BOOLEAN,
    work_place TEXT,
    work_start_date TEXT,
    work_address TEXT,
    public_sector BOOLEAN,
    work_phone TEXT,
    postgrad BOOLEAN,

    -- survey
    submitted BOOLEAN DEFAULT 0,

    -- personal
    email TEXT,
    home_address TEXT,
    marital_status_id INTEGER DEFAULT 1,

    -- academic
    postgrad_reason TEXT,

    -- work
    cv BLOB,
    cv_file_name TEXT,
    work_reason TEXT,
    work_position TEXT,

    -- feedback
    communicate BOOLEAN,
    follow BOOLEAN,
    club BOOLEAN,
    suggestion TEXT,
    FOREIGN KEY (id) REFERENCES users(id),
    FOREIGN KEY (major_id) REFERENCES majors(id),
    FOREIGN KEY (marital_status_id) REFERENCES marital_status(id),
    FOREIGN KEY (degree_id) REFERENCES degrees(id),
    FOREIGN KEY (nno_hash) REFERENCES users(password_hash)
);

CREATE UNIQUE INDEX alumni_username_index ON alumni (username);

CREATE TABLE alumni_posts (
    id INTEGER PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES posts(id)
);

CREATE TABLE social_links (
    id INTEGER PRIMARY KEY,
    alumni_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    link TEXT NOT NULL,
    FOREIGN KEY (alumni_id) REFERENCES alumni(id)
);

CREATE TABLE majors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO majors (name) VALUES ('Computer Science'), ('Software Engineering'), ('Information Systems'), ('Computer Graphics'), ('Information Security');

CREATE TABLE degrees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO degrees (name) VALUES ('Bachelor'), ('Master Thesis'), ('Master Comprehensive');

CREATE TABLE marital_status (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO marital_status (name) VALUES ('Unspecified'), ('Single'), ('Married'), ('Divorced'), ('Widowed');

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    publish_date TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE likes (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE dislikes (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE follows (
    id INTEGER PRIMARY KEY,
    follower_id INTEGER NOT NULL,
    following_id INTEGER NOT NULL,
    FOREIGN KEY (follower_id) REFERENCES users(id),
    FOREIGN KEY (following_id) REFERENCES users(id)
);

CREATE TABLE stats (
    -- counters
    alumni_count INTEGER DEFAULT 0,
    news_count INTEGER DEFAULT 0,
    posts_count INTEGER DEFAULT 0,
    comments_count INTEGER DEFAULT 0,
    likes_count INTEGER DEFAULT 0,
    dislikes_count INTEGER DEFAULT 0,

    -- bar chart --

    -- graduation year
    _2019_count INTEGER DEFAULT 0,
    _2020_count INTEGER DEFAULT 0,
    _2021_count INTEGER DEFAULT 0,
    _2022_count INTEGER DEFAULT 0,
    _2023_count INTEGER DEFAULT 0,

    -- dounut charts --

    -- gender
    male_count INTEGER DEFAULT 0,
    female_count INTEGER DEFAULT 0,

    -- work sector
    public_sector_count INTEGER DEFAULT 0,
    private_sector_count INTEGER DEFAULT 0,

    survey_submitted_count INTEGER DEFAULT 0,
    follow_count INTEGER DEFAULT 0,
    not_follow_count INTEGER DEFAULT 0,
    club_count INTEGER DEFAULT 0,
    not_club_count INTEGER DEFAULT 0,
    communicate_count INTEGER DEFAULT 0,
    not_communicate_count INTEGER DEFAULT 0,

    -- pie charts --

    -- work status
    work_count INTEGER DEFAULT 0,
    never_worked_count INTEGER DEFAULT 0,
    unspecified_work_count INTEGER DEFAULT 0,

    -- ratings
    excellent_count INTEGER DEFAULT 0,
    very_good_count INTEGER DEFAULT 0,
    good_count INTEGER DEFAULT 0,
    fair_count INTEGER DEFAULT 0,
    poor_count INTEGER DEFAULT 0,

    -- degrees
    bachelor_count INTEGER DEFAULT 0,
    master_thesis_count INTEGER DEFAULT 0,
    master_comprehensive_count INTEGER DEFAULT 0,

    -- martial status
    unspecified_marital_status_count INTEGER DEFAULT 0,
    single_count INTEGER DEFAULT 0,
    married_count INTEGER DEFAULT 0,
    divorced_count INTEGER DEFAULT 0,
    widowed_count INTEGER DEFAULT 0,

    -- majors
    computer_science_count INTEGER DEFAULT 0,
    software_engineering_count INTEGER DEFAULT 0,
    information_systems_count INTEGER DEFAULT 0,
    computer_graphics_count INTEGER DEFAULT 0,
    information_security_count INTEGER DEFAULT 0,

    -- graduation semester
    first_semester_count INTEGER DEFAULT 0,
    second_semester_count INTEGER DEFAULT 0,
    summer_count INTEGER DEFAULT 0,

    -- postgrad
    postgrad_count INTEGER DEFAULT 0,
    no_postgrad_count INTEGER DEFAULT 0,
    postgrad_unspecified_count INTEGER DEFAULT 0
);

INSERT INTO stats DEFAULT VALUES;

CREATE TRIGGER add_admin AFTER INSERT ON admins BEGIN
    INSERT INTO users (id, name) VALUES (NEW.id, NEW.username);
END;

CREATE TRIGGER add_alumni AFTER INSERT ON alumni BEGIN
    INSERT INTO users (id, name, phone_number, email) VALUES (NEW.id, NEW.full_name, NEW.phone_number, NEW.email);
    UPDATE stats SET alumni_count = alumni_count + 1;

    -- gender
    UPDATE stats SET male_count = male_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND gender = 0);
    UPDATE stats SET female_count = female_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND gender = 1);

    -- work
    UPDATE stats SET work_count = work_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND work = 1);
    UPDATE stats SET unspecified_work_count = unspecified_work_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND work IS NULL);

    -- work sector
    UPDATE stats SET public_sector_count = public_sector_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND public_sector = 1);
    UPDATE stats SET private_sector_count = private_sector_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND public_sector = 0);

    -- postgrad
    UPDATE stats SET postgrad_count = postgrad_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND postgrad = 1);
    UPDATE stats SET postgrad_unspecified_count = postgrad_unspecified_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND postgrad IS NULL);

    -- GPA
    UPDATE stats SET excellent_count = excellent_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND GPA >= 365);
    UPDATE stats SET very_good_count = very_good_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND GPA >= 300 AND GPA < 365);
    UPDATE stats SET good_count = good_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND GPA >= 250 AND GPA < 300);
    UPDATE stats SET fair_count = fair_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND GPA >= 200 AND GPA < 250);
    UPDATE stats SET poor_count = poor_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND GPA < 200);

    -- degreess
    UPDATE stats SET bachelor_count = bachelor_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND degree_id = (SELECT id FROM degrees WHERE name = 'Bachelor'));
    UPDATE stats SET master_thesis_count = master_thesis_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND degree_id = (SELECT id FROM degrees WHERE name = 'Master Thesis'));
    UPDATE stats SET master_comprehensive_count = master_comprehensive_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND degree_id = (SELECT id FROM degrees WHERE name = 'Master Comprehensive'));

    -- marital status
    UPDATE stats SET unspecified_marital_status_count = unspecified_marital_status_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Unspecified'));
    UPDATE stats SET single_count = single_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Single'));
    UPDATE stats SET married_count = married_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Married'));
    UPDATE stats SET divorced_count = divorced_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Divorced'));
    UPDATE stats SET widowed_count = widowed_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Widowed'));

    -- majors
    UPDATE stats SET computer_science_count = computer_science_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND major_id = (SELECT id FROM majors WHERE name = 'Computer Science'));
    UPDATE stats SET software_engineering_count = software_engineering_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND major_id = (SELECT id FROM majors WHERE name = 'Software Engineering'));
    UPDATE stats SET information_systems_count = information_systems_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND major_id = (SELECT id FROM majors WHERE name = 'Information Systems'));
    UPDATE stats SET computer_graphics_count = computer_graphics_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND major_id = (SELECT id FROM majors WHERE name = 'Computer Graphics'));
    UPDATE stats SET information_security_count = information_security_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND major_id = (SELECT id FROM majors WHERE name = 'Information Security'));

    -- graduation semester
    UPDATE stats SET first_semester_count = first_semester_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_semester = 1);
    UPDATE stats SET second_semester_count = second_semester_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_semester = 2);
    UPDATE stats SET summer_count = summer_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_semester = 3);

    -- graduation year
    UPDATE stats SET _2019_count = _2019_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_year = 2019);
    UPDATE stats SET _2020_count = _2020_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_year = 2020);
    UPDATE stats SET _2021_count = _2021_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_year = 2021);
    UPDATE stats SET _2022_count = _2022_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_year = 2022);
    UPDATE stats SET _2023_count = _2023_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND graduation_year = 2023);
END;

CREATE TRIGGER before_update_alumni_stats BEFORE UPDATE ON alumni BEGIN
    -- work
    UPDATE stats SET work_count = work_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND work = 1);
    UPDATE stats SET unspecified_work_count = unspecified_work_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND work IS NULL);
    UPDATE stats SET never_worked_count = never_worked_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND work = 0);

    -- marital status
    UPDATE stats SET unspecified_marital_status_count = unspecified_marital_status_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Unspecified'));
    UPDATE stats SET single_count = single_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Single'));
    UPDATE stats SET married_count = married_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Married'));
    UPDATE stats SET divorced_count = divorced_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Divorced'));
    UPDATE stats SET widowed_count = widowed_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Widowed'));

    -- postgrad
    UPDATE stats SET postgrad_count = postgrad_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND postgrad = 1);
    UPDATE stats SET postgrad_unspecified_count = postgrad_unspecified_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND postgrad IS NULL);
    UPDATE stats SET no_postgrad_count = no_postgrad_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND postgrad = 0);

    UPDATE stats SET follow_count = follow_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND follow = 1);
    UPDATE stats SET not_follow_count = not_follow_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND follow = 0);
    UPDATE stats SET club_count = club_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND club = 1);
    UPDATE stats SET not_club_count = not_club_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND club = 0);
    UPDATE stats SET communicate_count = communicate_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND communicate = 1);
    UPDATE stats SET not_communicate_count = not_communicate_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND communicate = 0);
    UPDATE stats SET survey_submitted_count = survey_submitted_count - (SELECT COUNT(*) FROM alumni WHERE id = OLD.id AND submitted = 1);
END;

CREATE TRIGGER after_update_alumni AFTER UPDATE ON alumni BEGIN
    UPDATE users SET phone_number = NEW.phone_number, email = NEW.email WHERE id = NEW.id;

    -- work
    UPDATE stats SET work_count = work_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND work = 1);
    UPDATE stats SET unspecified_work_count = unspecified_work_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND work IS NULL);
    UPDATE stats SET never_worked_count = never_worked_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND work = 0);

    -- marital status
    UPDATE stats SET unspecified_marital_status_count = unspecified_marital_status_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Unspecified'));
    UPDATE stats SET single_count = single_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Single'));
    UPDATE stats SET married_count = married_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Married'));
    UPDATE stats SET divorced_count = divorced_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Divorced'));
    UPDATE stats SET widowed_count = widowed_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND marital_status_id = (SELECT id FROM marital_status WHERE name = 'Widowed'));

    -- postgrad
    UPDATE stats SET postgrad_count = postgrad_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND postgrad = 1);
    UPDATE stats SET postgrad_unspecified_count = postgrad_unspecified_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND postgrad IS NULL);
    UPDATE stats SET no_postgrad_count = no_postgrad_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND postgrad = 0);

    UPDATE stats SET follow_count = follow_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND follow = 1);
    UPDATE stats SET not_follow_count = not_follow_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND follow = 0);
    UPDATE stats SET club_count = club_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND club = 1);
    UPDATE stats SET not_club_count = not_club_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND club = 0);
    UPDATE stats SET communicate_count = communicate_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND communicate = 1);
    UPDATE stats SET not_communicate_count = not_communicate_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND communicate = 0);
    UPDATE stats SET survey_submitted_count = survey_submitted_count + (SELECT COUNT(*) FROM alumni WHERE id = NEW.id AND submitted = 1);
END;

CREATE TRIGGER news_stats_increment AFTER INSERT ON news BEGIN
    UPDATE stats SET news_count = news_count + 1;
    UPDATE admins SET news_count = news_count + 1 WHERE id = NEW.user_id;
END;

CREATE TRIGGER news_stats_decrement BEFORE DELETE ON news BEGIN
    UPDATE stats SET news_count = news_count - 1;
    UPDATE admins SET news_count = news_count - 1 WHERE id = OLD.user_id;
END;

CREATE TRIGGER post_stats_increment AFTER INSERT ON posts BEGIN
    UPDATE stats SET posts_count = posts_count + 1;
    UPDATE users SET posts_count = posts_count + 1 WHERE id = NEW.user_id;
END;

CREATE TRIGGER post_stats_decrement BEFORE DELETE ON posts BEGIN
    UPDATE stats SET posts_count = posts_count - 1;
    UPDATE users SET posts_count = posts_count - 1 WHERE id = OLD.user_id;
END;

CREATE TRIGGER comment_stats_increment AFTER INSERT ON comments BEGIN
    UPDATE stats SET comments_count = comments_count + 1;
    UPDATE posts SET comments_count = comments_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET comments_count = comments_count + 1 WHERE id = NEW.user_id;
END;

CREATE TRIGGER comment_stats_decrement BEFORE DELETE ON comments BEGIN
    UPDATE stats SET comments_count = comments_count - 1;
    UPDATE posts SET comments_count = comments_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET comments_count = comments_count - 1 WHERE id = OLD.user_id;
END;

CREATE TRIGGER like_stats_increment AFTER INSERT ON likes BEGIN
    UPDATE stats SET likes_count = likes_count + 1;
    UPDATE posts SET likes_count = likes_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET likes_count = likes_count + 1 WHERE id = NEW.user_id;
END;

CREATE TRIGGER like_stats_decrement BEFORE DELETE ON likes BEGIN
    UPDATE stats SET likes_count = likes_count - 1;
    UPDATE posts SET likes_count = likes_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET likes_count = likes_count - 1 WHERE id = OLD.user_id;
END;

CREATE TRIGGER dislike_stats_increment AFTER INSERT ON dislikes BEGIN
    UPDATE stats SET dislikes_count = dislikes_count + 1;
    UPDATE posts SET dislikes_count = dislikes_count + 1 WHERE id = NEW.post_id;
    UPDATE users SET dislikes_count = dislikes_count + 1 WHERE id = NEW.user_id;
END;

CREATE TRIGGER dislike_stats_decrement BEFORE DELETE ON dislikes BEGIN
    UPDATE stats SET dislikes_count = dislikes_count - 1;
    UPDATE posts SET dislikes_count = dislikes_count - 1 WHERE id = OLD.post_id;
    UPDATE users SET dislikes_count = dislikes_count - 1 WHERE id = OLD.user_id;
END;

CREATE TRIGGER follow_stats_increment AFTER INSERT ON follows BEGIN
    UPDATE users SET following_count = following_count + 1 WHERE id = NEW.follower_id;
    UPDATE users SET followers_count = followers_count + 1 WHERE id = NEW.following_id;
END;

CREATE TRIGGER follow_stats_decrement BEFORE DELETE ON follows BEGIN
    UPDATE users SET following_count = following_count - 1 WHERE id = OLD.follower_id;
    UPDATE users SET followers_count = followers_count - 1 WHERE id = OLD.following_id;
END;