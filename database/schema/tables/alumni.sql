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
    submitted BOOLEAN DEFAULT FALSE,

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

    -- privacy settings
    personal_privacy BOOLEAN NOT NULL DEFAULT 1,
    academic_privacy BOOLEAN NOT NULL DEFAULT 1,
    employment_privacy BOOLEAN NOT NULL DEFAULT 1,

    FOREIGN KEY (id) REFERENCES users(id),
    FOREIGN KEY (major_id) REFERENCES majors(id),
    FOREIGN KEY (marital_status_id) REFERENCES marital_status(id),
    FOREIGN KEY (degree_id) REFERENCES degrees(id),
    FOREIGN KEY (nno_hash) REFERENCES users(password_hash)
);