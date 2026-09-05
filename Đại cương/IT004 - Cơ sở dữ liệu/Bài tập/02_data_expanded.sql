USE student_management;

-- Insert Faculties
INSERT INTO faculties(faculty_id, faculty_name, established_date) VALUES
('CSE', 'Faculty of Computer Science and Engineering', '2005-03-26'),
('BA', 'Faculty of Business Administration', '2008-01-15'),
('ME', 'Faculty of Mechanical Engineering', '2010-01-01'),
('EE', 'Faculty of Electrical Engineering', '2007-09-01');

-- Insert Rooms
INSERT INTO rooms(room_code, building, capacity) VALUES
('A101', 'A', 120), ('A102', 'A', 120), ('LAB_CSE', 'A', 60),
('B101', 'B', 80), ('B102', 'B', 80), ('C201', 'C', 60), ('D_HALL', 'D', 200),
('E301', 'E', 50), ('E302_LAB', 'E', 50);

-- Insert Lecturers
INSERT INTO lecturers(lecturer_code, full_name, email, gender, date_of_birth, start_date, degree, faculty_id) VALUES
('GV001', 'Nguyen Van Duc', 'gv001@uit.edu.vn', 'Male', '1980-05-20', '2006-09-01', 'PhD', 'CSE'),
('GV002', 'Tran Thi Ha', 'gv002@uit.edu.vn', 'Female', '1985-11-10', '2010-09-01', 'MSc', 'CSE'),
('GV003', 'Le Van Tai', 'gv003@uit.edu.vn', 'Male', '1975-10-20', '2005-09-01', 'PhD', 'BA'),
('GV004', 'Hoang Thi My', 'gv004@uit.edu.vn', 'Female', '1990-01-15', '2015-09-01', 'MSc', 'CSE'),
('GV005', 'Vu Tuan Anh', 'gv005@uit.edu.vn', 'Male', '1988-11-30', '2014-09-01', 'BSc', 'BA'),
('GV006', 'Phan Thanh Binh', 'gv006@uit.edu.vn', 'Male', '1978-02-15', '2009-01-20', 'AssocProf', 'EE'),
('GV007', 'Do Ngoc Mai', 'gv007@uit.edu.vn', 'Female', '1992-07-21', '2017-08-15', 'MSc', 'EE');

-- Insert Subjects
INSERT INTO subjects(subject_code, subject_name, credits, subject_type, faculty_id) VALUES
('CSDL01', 'Database Systems', 3, 'Core', 'CSE'), ('CTDLGT', 'Data Structures and Algorithms', 4, 'Core', 'CSE'),
('NMLT01', 'Introduction to Programming', 3, 'General', 'CSE'), ('MMT01', 'Computer Networks', 3, 'Core', 'CSE'),
('MKT01', 'Principles of Marketing', 3, 'Core', 'BA'), ('KTNH01', 'Introduction to Accounting', 3, 'Core', 'BA'),
('TRIET01', 'Philosophy of Marxism-Leninism', 2, 'General', 'CSE'), ('PLDC01', 'Introduction to Law', 2, 'General', 'CSE'),
('CIR01', 'Circuit Theory', 4, 'Core', 'EE'), ('SIG01', 'Signals and Systems', 3, 'Core', 'EE');

-- Insert Classes
INSERT INTO classes(class_code, class_name, faculty_id, academic_year) VALUES
('CSE21A', 'Computer Science K21A', 'CSE', 2021), ('BA21A', 'Business Admin K21A', 'BA', 2021),
('CSE22A', 'Computer Science K22A', 'CSE', 2022), ('BA22A', 'Business Admin K22A', 'BA', 2022),
('CSE23A', 'Computer Science K23A', 'CSE', 2023), ('EE22A', 'Electrical Eng K22A', 'EE', 2022);

-- Insert Students (More students for variety)
INSERT INTO students(student_code, full_name, date_of_birth, gender, email, class_id, enrollment_date) VALUES
-- K22 Students
('22520001', 'Le Quang Huy', '2004-08-19', 'Male', '22520001@uit.edu.vn', 3, '2022-09-05'),
('22520002', 'Pham Thi An', '2004-09-10', 'Female', '22520002@uit.edu.vn', 3, '2022-09-05'),
('22520003', 'Tran Van Binh', '2004-01-15', 'Male', '22520003@uit.edu.vn', 3, '2022-09-05'),
('22520004', 'Nguyen Thi Lan', '2004-03-20', 'Female', '22520004@uit.edu.vn', 3, '2022-09-05'),
('22480001', 'Dang Tuan Kiet', '2004-05-10', 'Male', '22480001@uit.edu.vn', 4, '2022-09-05'),
('22480002', 'Le Thi Mai', '2004-12-01', 'Female', '22480002@uit.edu.vn', 4, '2022-09-05'),
('22600001', 'Ly Minh Long', '2004-04-14', 'Male', '22600001@uit.edu.vn', 6, '2022-09-05'),
('22600002', 'Vu Thi Hong', '2004-06-25', 'Female', '22600002@uit.edu.vn', 6, '2022-09-05'),
-- K21 Students (older)
('21520001', 'Ha Quoc Tuan', '2003-08-10', 'Male', '21520001@uit.edu.vn', 1, '2021-09-05'),
('21520002', 'Tran Ngoc Linh', '2003-11-05', 'Female', '21520002@uit.edu.vn', 1, '2021-09-05'),
('21480001', 'Nguyen Hoang Viet', '2003-01-12', 'Male', '21480001@uit.edu.vn', 2, '2021-09-05');

-- Insert Tuition Fees for multiple semesters
INSERT INTO tuition_fees(semester, school_year, price_per_credit) VALUES
('SEM1', 2024, 600000), ('SEM2', 2024, 620000),
('SEM1', 2025, 650000), ('SEM2', 2025, 700000);

-- Insert Sections for SEM1/2025
INSERT INTO sections(section_code, subject_id, lecturer_id, semester, school_year) VALUES
('CSDL01_25_1', 1, 1, 'SEM1', 2025), ('CTDLGT_25_1', 2, 2, 'SEM1', 2025),
('MKT01_25_1', 5, 3, 'SEM1', 2025), ('TRIET01_25_1', 7, 5, 'SEM1', 2025),
('CSDL01_25_2', 1, 4, 'SEM1', 2025), ('MMT01_25_1', 4, 1, 'SEM1', 2025),
('CIR01_25_1', 9, 6, 'SEM1', 2025);

-- Insert Schedules for SEM1/2025 sections
INSERT INTO schedules(section_id, day_of_week, start_time, end_time, room_id, start_week, end_week) VALUES
(1, 2, '07:30:00', '09:30:00', 1, 1, 15), (1, 4, '07:30:00', '09:30:00', 1, 1, 15),
(2, 2, '09:45:00', '11:45:00', 3, 1, 15), (2, 4, '09:45:00', '11:45:00', 3, 1, 15),
(3, 3, '07:30:00', '09:30:00', 4, 1, 15), (3, 5, '07:30:00', '09:30:00', 4, 1, 15),
(4, 6, '09:45:00', '11:45:00', 7, 1, 10),
(5, 2, '07:30:00', '09:30:00', 2, 1, 15), (5, 4, '09:45:00', '11:45:00', 2, 1, 15),
(6, 5, '13:30:00', '16:30:00', 3, 1, 15),
(7, 3, '13:00:00', '15:00:00', 8, 1, 15), (7, 5, '13:00:00', '15:00:00', 9, 1, 15);

-- Insert Enrollments (will auto-trigger tuition calculation)
INSERT INTO enrollments(student_id, section_id, enrollment_date) VALUES
(1, 1, '2025-01-10'), (1, 2, '2025-01-10'), (2, 2, '2025-01-11'),
(3, 1, '2025-01-11'), (3, 4, '2025-01-11'), (4, 2, '2025-01-12'),
(4, 5, '2025-01-12'), (5, 3, '2025-01-11'), (5, 4, '2025-01-11'),
(6, 3, '2025-01-12'), (7, 7, '2025-01-13'), (8, 7, '2025-01-13'),
(9, 5, '2025-01-13'), (9, 6, '2025-01-14'), (10, 1, '2025-01-15');

-- Insert Grades
INSERT INTO grades(student_id, section_id, component_score, midterm_score, final_score) VALUES
(1, 1, 8.0, 7.5, 8.0), (1, 2, 9.0, 8.5, 9.5), (2, 2, 7.0, 6.0, 7.5),
(3, 1, 9.0, 8.0, 8.5), (3, 4, 7.0, 7.0, 7.0), (4, 2, 8.0, 9.0, 9.0),
(4, 5, 8.5, 8.0, 7.5), (5, 3, 7.5, 8.0, 9.0), (5, 4, 6.0, 6.0, 6.5),
(6, 3, 3.0, 2.0, 4.0), (7, 7, 8.5, 9.0, 9.0), (8, 7, 7.0, 7.5, 8.0),
(9, 5, 5.0, 6.0, 8.0), (9, 6, 4.0, 5.0, 3.0), (10, 1, 6.0, 6.5, 7.5);

-- Update some tuition invoice statuses
UPDATE tuition_invoices SET status = 'Paid' WHERE student_id IN (1, 5, 8);
UPDATE tuition_invoices SET status = 'Exempt' WHERE student_id = 4;