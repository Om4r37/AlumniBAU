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