CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);

INSERT INTO students VALUES (1, 'Amit', 85);
INSERT INTO students VALUES (2, 'Riya', 92);
INSERT INTO students VALUES (3, 'John', 78);

SELECT * FROM students;d. Code Examples
SELECT name, marks FROM students;

SELECT * FROM students WHERE marks > 80;
SELECT * FROM students WHERE marks > 80 AND name != 'John';
SELECT name FROM students WHERE marks >= 90;

CREATE TABLE scores (
    subject TEXT,
    marks INTEGER
);
INSERT INTO scores VALUES ('Math', 80);
INSERT INTO scores VALUES ('Math', 90);
INSERT INTO scores VALUES ('Science', 85);
SELECT subject, AVG(marks) FROM scores GROUP BY subject;
SELECT subject, COUNT(*) FROM scores GROUP BY subject;

CREATE TABLE departments (
    id INTEGER,
    dept TEXT
);
SELECT students.name, departments.dept
FROM students
INNER JOIN departments
ON students.id = departments.id;


--task 1 The Database Architect
CREATE TABLE interns(
    id INT,
    name TEXT,
    track TEXT,
    stipend INT
);
INSERT INTO interns VALUES (1, 'Alice', 'Data Science', 5000);
INSERT INTO interns VALUES (2, 'Bob', 'Web Development', 4500);
INSERT INTO interns VALUES (3, 'Charlie', 'Data Science', 5500);
INSERT INTO interns VALUES (4, 'David', 'Web Development', 4000);
INSERT INTO interns VALUES (5, 'Eve', 'Data Science', 6000);
SELECT name,track FROM interns;


