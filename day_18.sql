--task 1 The Insight Filter
SELECT name,track FROM interns;
SELECT * FROM interns WHERE stipend > 5000;
SELECT track, AVG(stipend) FROM interns GROUP BY track;
SELECT track, COUNT(*) FROM interns GROUP BY track;







































--task 2 The Data Connector
CREATE TABLE mentors (
    mentor_id INT,
    mentor_name TEXT,
    track TEXT
);
INSERT INTO mentors VALUES (1, 'Dr. Smith', 'Data Science');
INSERT INTO mentors VALUES (2, 'Ms. Johnson', 'Web Development');
INSERT INTO mentors VALUES (3, 'Dr. Lee', 'Data Science');
SELECT interns.name, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
