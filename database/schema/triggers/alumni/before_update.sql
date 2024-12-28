CREATE TRIGGER before_update_alumni BEFORE UPDATE ON alumni BEGIN
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