-- add Bonus procedure
-- adds a correction for a student
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    IF NOT EXISTS (
        SELECT * FROM projects
        WHERE name = project_name)
        BEGIN
            INSERT INTO projects (name) VALUES (project_name)
        END
    INSERT INTO corrections (user_id, project_id, score)
        VALUES (
            user_id,
            (SELECT id FROM projects WHERE name = project_name),
            score
        );
END