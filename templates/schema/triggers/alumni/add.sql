CREATE TRIGGER add_alumni AFTER INSERT ON alumni BEGIN
    INSERT INTO users (id, phone_number, email) VALUES (NEW.id, NEW.phone_number, NEW.email);
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