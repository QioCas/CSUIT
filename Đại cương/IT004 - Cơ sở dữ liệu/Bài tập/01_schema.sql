-- Drop the database if it exists to start fresh
DROP DATABASE IF EXISTS student_management;

-- Create the database with UTF8MB4 character set for full Unicode support
CREATE DATABASE student_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Select the newly created database for use
USE student_management;

-- ================================================================
--  TABLE DEFINITIONS
-- ================================================================

CREATE TABLE faculties (
  faculty_id   CHAR(4) PRIMARY KEY,
  faculty_name VARCHAR(100) NOT NULL,
  established_date DATE NULL
);

CREATE TABLE rooms (
  room_id     INT AUTO_INCREMENT PRIMARY KEY,
  room_code   VARCHAR(20) NOT NULL UNIQUE,
  building    VARCHAR(50),
  capacity    INT NOT NULL CHECK (capacity >= 10)
);

CREATE TABLE lecturers (
  lecturer_id   INT AUTO_INCREMENT PRIMARY KEY,
  lecturer_code VARCHAR(10) NOT NULL UNIQUE,
  full_name     VARCHAR(100) NOT NULL,
  email         VARCHAR(120) UNIQUE,
  gender        ENUM('Male','Female') NOT NULL,
  date_of_birth DATE NOT NULL,
  start_date    DATE NOT NULL,
  degree        ENUM('BSc','Eng','MSc','PhD','AssocProf') DEFAULT 'BSc',
  faculty_id    CHAR(4) NOT NULL,
  FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id),
  CHECK (TIMESTAMPDIFF(YEAR, date_of_birth, start_date) >= 22)
);

CREATE TABLE classes (
  class_id      INT AUTO_INCREMENT PRIMARY KEY,
  class_code    VARCHAR(20) NOT NULL UNIQUE,
  class_name    VARCHAR(100) NOT NULL,
  faculty_id    CHAR(4) NOT NULL,
  academic_year INT NOT NULL CHECK (academic_year BETWEEN 2000 AND 2100),
  FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id)
);

CREATE TABLE subjects (
  subject_id   INT AUTO_INCREMENT PRIMARY KEY,
  subject_code VARCHAR(20) NOT NULL UNIQUE,
  subject_name VARCHAR(120) NOT NULL,
  credits      TINYINT NOT NULL CHECK (credits BETWEEN 1 AND 8),
  subject_type ENUM('General','Core','Major','Elective') NOT NULL,
  faculty_id   CHAR(4) NOT NULL,
  FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id)
);

CREATE TABLE students (
  student_id      INT AUTO_INCREMENT PRIMARY KEY,
  student_code    VARCHAR(12) NOT NULL UNIQUE,
  full_name       VARCHAR(100) NOT NULL,
  date_of_birth   DATE NOT NULL,
  gender          ENUM('Male','Female') NOT NULL,
  email           VARCHAR(120) UNIQUE,
  class_id        INT NOT NULL,
  enrollment_date DATE NOT NULL,
  FOREIGN KEY (class_id) REFERENCES classes(class_id),
  CHECK (enrollment_date > date_of_birth)
);

CREATE TABLE sections (
  section_id      INT AUTO_INCREMENT PRIMARY KEY,
  section_code    VARCHAR(30) NOT NULL UNIQUE,
  subject_id      INT NOT NULL,
  lecturer_id     INT NOT NULL,
  semester        ENUM('SEM1','SEM2','SEM3') NOT NULL,
  school_year     INT NOT NULL CHECK (school_year BETWEEN 2000 AND 2100),
  default_room_id INT NULL,
  FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
  FOREIGN KEY (lecturer_id) REFERENCES lecturers(lecturer_id),
  FOREIGN KEY (default_room_id) REFERENCES rooms(room_id)
);

CREATE TABLE schedules (
  schedule_id INT AUTO_INCREMENT PRIMARY KEY,
  section_id  INT NOT NULL,
  day_of_week TINYINT NOT NULL COMMENT '2=Monday, 3=Tuesday, ..., 8=Sunday' CHECK (day_of_week BETWEEN 2 AND 8),
  start_time  TIME NOT NULL,
  end_time    TIME NOT NULL,
  room_id     INT NOT NULL,
  start_week  TINYINT NOT NULL CHECK (start_week BETWEEN 1 AND 53),
  end_week    TINYINT NOT NULL CHECK (end_week BETWEEN 1 AND 53),
  FOREIGN KEY (section_id) REFERENCES sections(section_id) ON DELETE CASCADE,
  FOREIGN KEY (room_id) REFERENCES rooms(room_id),
  CHECK (start_time < end_time),
  CHECK (start_week <= end_week)
);

CREATE TABLE grades (
  student_id      INT NOT NULL,
  section_id      INT NOT NULL,
  component_score DECIMAL(4,2) DEFAULT 0,
  midterm_score   DECIMAL(4,2) DEFAULT 0,
  final_score     DECIMAL(4,2) DEFAULT 0,
  total_score     DECIMAL(4,2) GENERATED ALWAYS AS (ROUND(0.1*component_score + 0.3*midterm_score + 0.6*final_score, 2)) STORED,
  result          ENUM('Pass','Fail') DEFAULT NULL,
  PRIMARY KEY (student_id, section_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

CREATE TABLE enrollments (
  student_id      INT NOT NULL,
  section_id      INT NOT NULL,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (student_id, section_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

CREATE TABLE tuition_fees (
  fee_id           INT AUTO_INCREMENT PRIMARY KEY,
  semester         ENUM('SEM1','SEM2','SEM3') NOT NULL,
  school_year      INT NOT NULL CHECK (school_year BETWEEN 2000 AND 2100),
  price_per_credit DECIMAL(12,0) NOT NULL CHECK (price_per_credit >= 0),
  UNIQUE KEY uq_fee_period (semester, school_year)
);

CREATE TABLE tuition_invoices (
  invoice_id    INT AUTO_INCREMENT PRIMARY KEY,
  student_id    INT NOT NULL,
  semester      ENUM('SEM1','SEM2','SEM3') NOT NULL,
  school_year   INT NOT NULL CHECK (school_year BETWEEN 2000 AND 2100),
  total_credits INT NOT NULL DEFAULT 0,
  amount        DECIMAL(15,0) NOT NULL DEFAULT 0,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status        ENUM('Pending','Paid','Exempt') DEFAULT 'Pending',
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  UNIQUE KEY uq_invoice (student_id, semester, school_year)
);

-- ==================================================
-- VIEWS
-- ==================================================
CREATE OR REPLACE VIEW v_grade_report AS
SELECT st.student_code, st.full_name, sec.section_code, sub.subject_code, sub.subject_name,
       sec.semester, sec.school_year, g.component_score, g.midterm_score, g.final_score, g.total_score, g.result
FROM grades g
JOIN students st ON st.student_id = g.student_id
JOIN sections sec ON sec.section_id = g.section_id
JOIN subjects sub ON sub.subject_id = sec.subject_id;

CREATE OR REPLACE VIEW v_student_timetable AS
SELECT st.student_code, st.full_name, sec.section_code, sub.subject_name, sch.day_of_week,
       sch.start_time, sch.end_time, r.room_code, sec.semester, sec.school_year
FROM enrollments e
JOIN students st ON st.student_id = e.student_id
JOIN sections sec ON sec.section_id = e.section_id
JOIN subjects sub ON sub.subject_id = sec.subject_id
JOIN schedules sch ON sch.section_id = sec.section_id
JOIN rooms r ON r.room_id = sch.room_id;

CREATE OR REPLACE VIEW v_student_tuition AS
SELECT st.student_code, st.full_name, inv.semester, inv.school_year,
       inv.total_credits, inv.amount, inv.status
FROM tuition_invoices inv
JOIN students st ON st.student_id = inv.student_id;