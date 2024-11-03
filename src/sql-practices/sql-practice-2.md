# Практична Робота №2

1. **Завдання №1,2,3 (Створення таблиць, зв`язки між таблицями, заповнення даними)**

    
    ```sql
    
    -- Створення бази данихCourseAssignmentsCourseAssignments
    USE AdvancedUniversity;
    
    -- Завдання №1 (Створення таблиць), №2 (Звязки між таблицями), №3 ( Заповнення даними)
    -- Таблиця Students
    CREATE TABLE Students (
        StudentID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        DateOfBirth DATE,
        EnrollmentDate DATE,
        Status VARCHAR(20)
    );
    
    -- Заповнення таблиці Students
    INSERT INTO Students (FirstName, LastName, DateOfBirth, EnrollmentDate) VALUES
    ('Alex', 'Peterson', '1999-03-15', '2017-09-01'),
    ('Mia', 'Thompson', '2000-04-25', '2018-09-01'),
    ('Lucas', 'Evans', '1998-12-10', '2016-09-01'),
    ('Sophia', 'Mitchell', '2002-06-05', '2020-09-01'),
    ('Oliver', 'Harris', '2001-01-22', '2019-09-01'),
    ('Emma', 'Clark', '1999-11-19', '2017-09-01');
    
    -- Таблиця Courses
    CREATE TABLE Courses (
        CourseID INT PRIMARY KEY AUTO_INCREMENT,
        CourseName VARCHAR(100),
        Credits INT
    );
    
    -- Заповнення таблиці Courses
    INSERT INTO Courses (CourseName, Credits) VALUES
    ('Machine Learning', 4),
    ('Data Mining', 3),
    ('Cybersecurity', 3),
    ('Advanced Algorithms', 4),
    ('Web Development', 3),
    ('Artificial Intelligence', 3);
    
    -- Таблиця Enrollments
    CREATE TABLE Enrollments (
        EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
        StudentID INT,
        CourseID INT,
        Grade DECIMAL(3, 2),
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
    );
    
    -- Заповнення таблиці Enrollments
    INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES
    (1, 2, 3.6),  -- Alex Peterson -> Data Mining
    (1, 3, 3.8),  -- Alex Peterson -> Cybersecurity
    (2, 1, 4.0),  -- Mia Thompson -> Machine Learning
    (2, 4, 3.9),  -- Mia Thompson -> Advanced Algorithms
    (3, 2, 2.7),  -- Lucas Evans -> Data Mining
    (3, 4, 3.5),  -- Lucas Evans -> Advanced Algorithms
    (4, 1, 4.3),  -- Sophia Mitchell -> Machine Learning
    (4, 5, 3.2),  -- Sophia Mitchell -> Web Development
    (5, 3, 4.4),  -- Oliver Harris -> Cybersecurity
    (5, 6, 3.7),  -- Oliver Harris -> Artificial Intelligence
    (6, 2, 3.3),  -- Emma Clark -> Data Mining (єдиний запис для неї)
    (6, 5, 3.6);  -- Emma Clark -> Web Development (новий курс для різноманітності)
    
    -- Таблиця Professors
    CREATE TABLE Professors (
        ProfessorID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        HireDate DATE,
        DepartmentID INT
    );
    
    -- Заповнення таблиці Professors
    INSERT INTO Professors (FirstName, LastName, HireDate, DepartmentID) VALUES
    ('John', 'Taylor', '2014-02-12', 1),
    ('Anna', 'Smith', '2013-06-18', 1),
    ('Mark', 'Davis', '2017-05-09', 2),
    ('Rachel', 'Brown', '2019-11-23', 2),
    ('David', 'White', '2021-02-15', 3),
    ('Lisa', 'Moore', '2020-07-27', 3);
    
    -- Таблиця Departments
    CREATE TABLE Departments (
        DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(100),
        HeadOfDepartment INT,
        FOREIGN KEY (HeadOfDepartment) REFERENCES Professors(ProfessorID)
    );
    
    -- Заповнення таблиці Departments
    INSERT INTO Departments (DepartmentName, HeadOfDepartment) VALUES
    ('Computer Science', 1),
    ('Mathematics', 3),
    ('Cybersecurity', 4),
    ('Engineering', 5),
    ('Robotics', 6);
    
    -- Таблиця CourseAssignments для зв'язку курсів та викладачів
    CREATE TABLE CourseAssignments (
        CourseAssignmentID INT PRIMARY KEY AUTO_INCREMENT,
        CourseID INT,
        ProfessorID INT,
        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
        FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
    );
    
    -- Заповнення таблиці CourseAssignments
    INSERT INTO CourseAssignments (CourseID, ProfessorID) VALUES
    (1, 1),  -- Machine Learning викладає John Taylor
    (2, 2),  -- Data Mining викладає Anna Smith
    (3, 3),  -- Cybersecurity викладає Mark Davis
    (4, 4),  -- Advanced Algorithms викладає Rachel Brown
    (5, 5),  -- Web Development викладає David White
    (6, 6);  -- Artificial Intelligence викладає Lisa Moore
    
    ```
    

Результати виконання SELECT запитів:

1. SELECT * FROM AdvancedUniversity.Students

![Select AdvancedUniversity.Students.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/21a59c93-76bd-4c12-b424-a0012d41e2c3.png)

1. SELECT * FROM AdvancedUniversity.Courses

![Select Courses.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/0866fd7c-c291-4247-90b6-8f36934595e4.png)

1. SELECT * FROM AdvancedUniversity.Enrollments

![Select Enrollments.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/e2682627-7353-45fe-853b-7c5b634d0567.png)

1. SELECT * FROM AdvancedUniversity.Professors

![Select AdvancedUniversity.Professors.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/696745ab-0b18-4092-893e-05ca9b0589d9.png)

1. SELECT * FROM AdvancedUniversity.Departments

![Select AdvancedUniversity.Departments.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/75212fc5-f8ee-43a5-b424-e826f4d047e2.png)

1. SELECT * FROM AdvancedUniversity.CourseAssignments

![Select AdvancedUnivesity.CourseAssignments.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/6f38c41b-92b1-47ba-886c-76d00823f061.png)

1. **Завдання №4 (Робота з агрегатними функціями та угрупуванням)**

```sql
-- №4 (Робота з агрегатними функціями та угрупованням)
-- Середня оцінка кожного студента за всі курси:
SELECT StudentID, AVG(Grade) AS AverageGrade
FROM Enrollments
GROUP BY StudentID;

-- Кількість курсів, які викладає кожен професор
SELECT ProfessorID, COUNT(CourseID) AS CourseCount
FROM CourseAssignments
GROUP BY ProfessorID;

-- Загальна кількість студентів на кожному курсі
SELECT CourseID, COUNT(StudentID) AS StudentCount
FROM Enrollments
GROUP BY CourseID;
```

Результати виконання:

1. Середня оцінка

![Screenshot 2024-11-03 at 4.06.44 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/2aa1cc9f-5392-4abd-a825-5167a64edb64.png)

1. Кількість курсів, які викладає кожен професор

![Screenshot 2024-11-03 at 4.07.18 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/3c97cf1d-09fd-42a7-92f3-bc782cd29785.png)

1. Загальна кількість студентів на кожному курсі

![Screenshot 2024-11-03 at 4.07.30 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/6fc6a6e0-d86e-48b5-9546-14fb0653accc.png)

1. **Завдання №5 (Використання JOIN операцій)**

```sql
-- №5 (Викорстання JOIN-операцій)
-- INNER JOIN для отримання інформації про студентів, курсів та викладачів
SELECT Students.FirstName AS StudentFirstName, Students.LastName AS StudentLastName,
       Courses.CourseName, 
       Professors.FirstName AS ProfessorFirstName, Professors.LastName AS ProfessorLastName
FROM Enrollments
INNER JOIN Students ON Enrollments.StudentID = Students.StudentID
INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
INNER JOIN CourseAssignments ON Courses.CourseID = CourseAssignments.CourseID
INNER JOIN Professors ON CourseAssignments.ProfessorID = Professors.ProfessorID;

-- емуляція FULL OUTER JOIN для відображення всіх студентів і курсів
SELECT Students.FirstName, Students.LastName, Courses.CourseName
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
LEFT JOIN Courses ON Enrollments.CourseID = Courses.CourseID
UNION
SELECT Students.FirstName, Students.LastName, Courses.CourseName
FROM Courses
LEFT JOIN Enrollments ON Courses.CourseID = Enrollments.CourseID
LEFT JOIN Students ON Enrollments.StudentID = Students.StudentID;
```

Результати виконання:
1. Inner join для отримання інформації про студентів, курсів та викладачів

![Screenshot 2024-11-03 at 4.25.19 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.25.19_PM.png)

1. емуляція FULL OUTER JOIN для відображення всіх студентів і курсів

![Screenshot 2024-11-03 at 4.25.25 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.25.25_PM.png)

1. **Завдання №6 (Інтерактивний запит із підзапитами)**

```sql
-- №6
-- Інтерактивний запит із підзапитами
SELECT FirstName, LastName
FROM Students
WHERE StudentID IN (
    SELECT StudentID
    FROM Enrollments
    WHERE Grade > (
        SELECT AVG(Grade)
        FROM Enrollments AS AvgGrades
        WHERE AvgGrades.CourseID = Enrollments.CourseID
    )
);

```

Результат виконання:
1. Студенти з оцінкою вище, ніж середня

![Screenshot 2024-11-03 at 4.30.10 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.30.10_PM.png)

1. **Завдання №7 (Оптимізація запитів)**

```sql
-- Оптимізація запитів
EXPLAIN SELECT StudentID, AVG(Grade) AS AverageGrade
FROM Enrollments
GROUP BY StudentID;

-- Аналіз: У цьому запиті MySQL має групувати результати за StudentID. Якщо у таблиці Enrollments багато записів і немає індексування - пошук по таблиці може бути повільним.
-- Рішення: 
CREATE INDEX idx_enrollments_studentid ON Enrollments(StudentID);
EXPLAIN SELECT ProfessorID, COUNT(CourseID) AS CourseCount
FROM CourseAssignments
GROUP BY ProfessorID;

-- Аналіз: Цей запит вираховує кількість курсів для кожного професора, що передбачає сканування великої кількості записів.
-- Рішення:
CREATE INDEX idx_courseassignments_professorid ON CourseAssignments(ProfessorID);
EXPLAIN SELECT CourseID, COUNT(StudentID) AS StudentCount
FROM Enrollments
GROUP BY CourseID;

-- Аналіз: Запит використовує GROUP BY CourseID, тому індекс на CourseID допоможе зменшити кількість сканованих записів.
-- Рішення:
CREATE INDEX idx_enrollments_courseid ON Enrollments(CourseID);
EXPLAIN SELECT Students.FirstName AS StudentFirstName, Students.LastName AS StudentLastName,
           Courses.CourseName, 
           Professors.FirstName AS ProfessorFirstName, Professors.LastName AS ProfessorLastName
FROM Enrollments
INNER JOIN Students ON Enrollments.StudentID = Students.StudentID
INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID
INNER JOIN CourseAssignments ON Courses.CourseID = CourseAssignments.CourseID
INNER JOIN Professors ON CourseAssignments.ProfessorID = Professors.ProfessorID;

-- Аналіз: Оскільки запит виконує кілька JOIN операцій, MySQL буде використовувати індекси на стовпцях, які беруть участь у з'єднаннях (JOIN).
-- Рішення:
CREATE INDEX idx_students_studentid ON Students(StudentID);
CREATE INDEX idx_courses_courseid ON Courses(CourseID);
CREATE INDEX idx_courseassignments_courseid ON CourseAssignments(CourseID);
CREATE INDEX idx_professors_professorid ON Professors(ProfessorID);
```

![Screenshot 2024-11-03 at 4.34.31 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.34.31_PM.png)

1. **Завдання №8 (Транзакції)**

```sql
-- Транзакції
START TRANSACTION;

UPDATE Enrollments SET Grade = 4.2 WHERE EnrollmentID = 2;
UPDATE Students SET LastName = 'Smith' WHERE StudentID = 2;

-- У разі помилки:
ROLLBACK;

-- Перевірка
SELECT * FROM AdvancedUniversity.Students as s where s.StudentID = 2;
SELECT * FROM AdvancedUniversity.Enrollments as e where e.EnrollmentID = 2;

-- Якщо все успішно:
COMMIT;
```

Результат виконання:
1. Update

![Screenshot 2024-11-03 at 4.42.15 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.42.15_PM.png)

1. SELECT * FROM AdvancedUniversity.Students as s where s.StudentID = 2;

![Screenshot 2024-11-03 at 4.41.30 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.41.30_PM.png)

1. SELECT * FROM AdvancedUniversity.enrollments as e where e.EnrollmentID = 2;

![Screenshot 2024-11-03 at 4.41.35 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.41.35_PM.png)

7. **Завдання №10 (Користувацькі функції та процедури)**

7.1 Функція для вирахування середньої оцінки студента

```sql
-- Функція для отримання середньої оцінки студента
DELIMITER //
CREATE FUNCTION GetStudentAverageGrade(student_id INT) 
RETURNS DECIMAL(3, 2)
DETERMINISTIC
BEGIN
    DECLARE avg_grade DECIMAL(3, 2);
    SELECT AVG(Grade) INTO avg_grade
    FROM Enrollments
    WHERE StudentID = student_id;
    RETURN avg_grade;
END //
DELIMITER ;

SHOW FUNCTION STATUS WHERE Name = 'GetStudentAverageGrade';
SELECT GetStudentAverageGrade(1) AS AverageGradeForStudent1;
```

Результат виконання:

![Screenshot 2024-11-03 at 4.49.43 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.49.43_PM.png)

7.2. Процедура по оновленню статуса студента (відмінник, добре тощо). на основі його оцінки

```sql
DELIMITER //
CREATE PROCEDURE UpdateStudentStatus(IN student_id INT)
BEGIN
    DECLARE avg_grade DECIMAL(3, 2);
    DECLARE status VARCHAR(20);

    SELECT AVG(Grade) INTO avg_grade
    FROM Enrollments
    WHERE StudentID = student_id;

    IF avg_grade IS NULL THEN
        SET status = 'Не визначено';
    ELSEIF avg_grade >= 4.5 THEN
        SET status = 'Відмінник';
    ELSEIF avg_grade >= 3.5 THEN
        SET status = 'Добре';
    ELSE
        SET status = 'Задовільно';
    END IF;

    UPDATE Students
    SET Status = status
    WHERE StudentID = student_id;
END //
DELIMITER ;

-- Перед оновленням
SELECT Status FROM Students WHERE StudentID = 1;
-- Виклик процедури
CALL UpdateStudentStatus(1);
-- Після оновлення
SELECT Status FROM Students WHERE StudentID = 1;
```

Результат Виконання:
1. Перед оновленням

![Screenshot 2024-11-03 at 4.53.21 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.53.21_PM.png)

1. Після оновлення

![Screenshot 2024-11-03 at 4.53.33 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_4.53.33_PM.png)

8. **Завдання на наданню доступів**

```sql
CREATE USER 'student'@'localhost' IDENTIFIED BY 'Student';
CREATE USER 'professor'@'localhost' IDENTIFIED BY 'Professor';
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

GRANT SELECT ON AdvancedUniversity.Students TO 'student'@'localhost';
GRANT SELECT, INSERT, UPDATE ON AdvancedUniversity.Enrollments TO 'professor'@'localhost';
GRANT ALL PRIVILEGES ON AdvancedUniversity.* TO 'admin'@'localhost';
```

![Screenshot 2024-11-03 at 5.00.29 PM.png](%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%B0%20%D0%A0%D0%BE%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%962%2013346d4316e180af8143e4ad7950be3b/Screenshot_2024-11-03_at_5.00.29_PM.png)