-- add Bonus procedure
-- adds a correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus (
  IN user_id int,
  IN project_name varchar(255),
  IN score float)
BEGIN
    DECLARE p_name VARCHAR(255);
    SELECT id INTO p_name FROM projects WHERE name = project_name;
    IF p_name IS NULL
    THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT id INTO p_name FROM projects WHERE name = project_name;
    END IF;

    -- IF NOT EXISTS (SELECT * FROM projects
    --                 WHERE name = project_name)
    -- BEGIN
    --     INSERT INTO projects (name) VALUES (project_name)
    -- END If
                    
    INSERT INTO corrections (user_id, project_id, score)
        VALUES (
            user_id,
            p_name,
            score
        );
END
$$