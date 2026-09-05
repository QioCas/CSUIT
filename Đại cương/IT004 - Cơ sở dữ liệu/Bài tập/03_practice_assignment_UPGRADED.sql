-- =============================================================
--  BUỔI 1: TRUY VẤN CƠ BẢN & LỌC DỮ LIỆU (with edge cases)
-- =============================================================

-- Q1.1 BEGIN
-- Lấy danh sách tất cả các Khoa (`faculties`).
-- Yêu cầu: output ít nhất (faculty_id, faculty_name).
-- Q1.1 END

-- Q1.2 BEGIN
-- Lấy danh sách sinh viên Nữ. Hiển thị: MSSV, Họ tên, Ngày sinh.
-- Q1.2 END

-- Q1.3 BEGIN
-- Lấy danh sách các môn học thuộc loại 'Core' VÀ có 4 tín chỉ.
-- Q1.3 END

-- Q1.4 BEGIN
-- Lấy danh sách giảng viên có họ bắt đầu bằng 'Nguyen' (không phân biệt hoa/thường; bỏ dấu nếu CSDL có collation phù hợp).
-- Gợi ý: dùng LOWER() hoặc thiết lập collation không phân biệt accent nếu có.
-- Q1.4 END

-- Q1.5 BEGIN
-- Lấy danh sách các phòng học ở 'Tòa nhà A' có sức chứa > 60, sắp xếp giảm dần theo sức chứa.
-- Q1.5 END

-- Q1.6 BEGIN
-- Lấy danh sách lịch học diễn ra vào Thứ 2 (day_of_week=2) và bắt đầu trước 09:00.
-- Q1.6 END

-- Q1.7 BEGIN
-- Lấy danh sách sinh viên nhập học trong tháng 9 năm 2022.
-- Viết HAI CÁCH: (a) dùng BETWEEN trên DATE; (b) dùng YEAR() & MONTH().
-- Q1.7 END

-- Q1.8 BEGIN
-- Lấy danh sách các môn học KHÔNG thuộc Khoa 'CSE' (tránh bẫy NULL khi dùng NOT IN).
-- Q1.8 END

-- Q1.9 BEGIN
-- Lấy 5 giảng viên được vào làm gần đây nhất.
-- Q1.9 END

-- Q1.10 BEGIN
-- Lấy danh sách các lớp học phần (`sections`) thuộc học kỳ 'SEM1' của năm học 2025.
-- Q1.10 END


-- =============================================================
--  BUỔI 2: GROUP BY, HAVING, JOIN (with business rules)
-- =============================================================

-- Q2.1 BEGIN
-- Đếm số lượng sinh viên trong mỗi lớp (`classes`). Output: class_code, class_name, student_count.
-- Q2.1 END

-- Q2.2 BEGIN
-- Đếm số lượng giảng viên trong mỗi khoa. Output: faculty_name, num_instructors.
-- Q2.2 END

-- Q2.3 BEGIN
-- Tính điểm trung bình (total_score) cho từng lớp học phần (section). Output: section_code, avg_total_score (DESC).
-- BỎ CÁC BẢN GHI có thành phần điểm NULL (coi là chưa đủ dữ kiện).
-- Q2.3 END

-- Q2.4 BEGIN
-- Đếm số lượng sinh viên 'Pass' và 'Fail' của lớp học phần có section_id = 1.
-- Q2.4 END

-- Q2.5 BEGIN
-- Liệt kê sinh viên đã đăng ký từ 2 MÔN trở lên trong SEM1/2025.
-- Không tính các section có status='CANCELLED' (nếu cột này tồn tại).
-- Q2.5 END

-- Q2.6 BEGIN
-- Tính tổng số tín chỉ mà mỗi sinh viên đã đăng ký trong SEM1/2025.
-- So khớp chéo số TC lấy từ subjects.credits; có thể cross-check với v_grade_report nếu đã tồn tại.
-- Q2.6 END

-- Q2.7 BEGIN
-- Tìm giảng viên đã dạy nhiều lớp học phần nhất trong SEM1/2025.
-- Tie-break: nếu số LHP bằng nhau, ưu tiên người có số SV đăng ký DISTINCT cao hơn.
-- Q2.7 END

-- Q2.8 BEGIN
-- Tính tổng số tiền học phí dự kiến theo trạng thái ('Pending','Paid') trong SEM1/2025.
-- Q2.8 END

-- Q2.9 BEGIN
-- Đếm số lượng môn học theo từng loại (subject_type).
-- Q2.9 END

-- Q2.10 BEGIN
-- Liệt kê các lớp (classes) có sĩ số > 3 sinh viên.
-- Q2.10 END


-- =============================================================
--  BUỔI 3: JOIN PHỨC TẠP, SUBQUERY, CTE, WINDOW
-- =============================================================

-- Q3.1 BEGIN
-- Lấy danh sách sinh viên và điểm thi môn 'Database Systems' (subject_code='CSDL01') trong SEM1/2025.
-- Q3.1 END

-- Q3.2 BEGIN
-- LEFT JOIN: Liệt kê TẤT CẢ các môn học và số lượng lớp học phần tương ứng trong SEM1/2025, kể cả môn chưa được mở lớp.
-- Thêm cột has_section = 0/1.
-- Q3.2 END

-- Q3.3 BEGIN
-- Subquery NOT IN/NOT EXISTS: Liệt kê các sinh viên CHƯA ĐĂNG KÝ môn nào trong SEM1/2025.
-- Tránh bẫy NULL (ưu tiên NOT EXISTS).
-- Q3.3 END

-- Q3.4 BEGIN
-- Subquery: Liệt kê SV có total_score trong section_id=1 cao hơn điểm trung bình của chính section đó.
-- Q3.4 END

-- Q3.5 BEGIN
-- CTE + WINDOW: Tìm Khoa có điểm trung bình chung của sinh viên cao nhất.
-- YÊU CẦU dùng RANK() OVER (ORDER BY gpa DESC) và chọn rank=1 (không dùng LIMIT 1).
-- Q3.5 END

-- Q3.6 BEGIN
-- View: Dùng v_grade_report, tìm các sinh viên KHÔNG RỚT MÔN NÀO (toàn 'Pass').
-- Q3.6 END

-- Q3.7 BEGIN
-- View: Dùng v_student_timetable, lấy TKB của sinh viên '22520001' vào Thứ 2 trong SEM1/2025.
-- Q3.7 END

-- Q3.8 BEGIN
-- LEFT JOIN ... IS NULL: Liệt kê TẤT CẢ sinh viên và số môn đã đăng ký (kể cả 0).
-- Gợi ý thêm cột num_passed nếu muốn tự kiểm.
-- Q3.8 END

-- Q3.9 BEGIN
-- Subquery IN: Liệt kê các giảng viên đã dạy các môn học thuộc khoa 'CSE' quản lý (DISTINCT theo gv_id).
-- Q3.9 END

-- Q3.10 BEGIN
-- Correlated EXISTS: Liệt kê các khoa có ít nhất một giảng viên có học vị 'PhD'.
-- Q3.10 END

-- Q3.11 BEGIN
-- Recursive CTE (Prerequisite chain): với subject_prereq(subject_id, prereq_subject_id):
-- (a) Liệt kê toàn bộ chuỗi tiên quyết cho mỗi môn (có cột depth).
-- (b) Phát hiện cycle (nếu có). Chỉ ra subject_id gây cycle.
-- Q3.11 END

-- Q3.12 BEGIN
-- Room utilization: Tính % sử dụng phòng = tổng giờ dạy / (5 ngày * 8 giờ).
-- Lọc phòng có utilization > 0.8, sắp xếp giảm dần. Return top-10.
-- Q3.12 END


-- =============================================================
--  BUỔI 4: TRIGGER, PROCEDURE, SIGNAL (ADVANCED)
-- =============================================================
DELIMITER $$

-- Q4.1 BEGIN
-- Trigger: trg_grades_set_result_before_insert & trg_grades_set_result_before_update
-- Yêu cầu:
--   - Kiểm tra component scores ∈ [0,10]; nếu sai -> SIGNAL SQLSTATE '45000' MESSAGE_TEXT='Invalid score range'.
--   - Set result = 'Pass' nếu total_score >= 5, ngược lại 'Fail'.
-- Gợi ý: total_score là GENERATED; dựa vào các cột thành phần hoặc dùng NEW.total_score nếu khả dụng.
-- VIẾT TRIGGER CỦA BẠN TẠI ĐÂY
-- Q4.1 END $$

-- Q4.2 BEGIN
-- Stored Procedure: sp_recalculate_tuition(IN p_student_id INT, IN p_semester VARCHAR(10), IN p_year INT)
-- Yêu cầu:
--   - Tính số tín chỉ đã đăng ký của SV trong kỳ.
--   - Lấy đơn giá/tín chỉ từ bảng price list tương ứng (tuition_prices).
--   - Ghi/ cập nhật (idempotent) vào tuition_invoices bằng INSERT ... ON DUPLICATE KEY UPDATE.
--   - Nếu thiếu bảng giá -> SIGNAL 'Tuition price not found'.
-- Triggers:
--   - trg_enrollment_after_insert/after_delete: gọi SP sau mỗi đăng ký/hủy đăng ký.
-- VIẾT STORED PROCEDURE & TRIGGERS CỦA BẠN TẠI ĐÂY
-- Q4.2 END $$

-- Q4.3 BEGIN
-- Trigger: trg_schedule_room_conflict_insert (BEFORE INSERT ON schedules)
-- Chặn thêm lịch nếu trùng phòng/ ngày/ khoảng giờ & khoảng tuần giao nhau.
-- Điều kiện trùng (t là dòng cũ, NEW là dòng mới):
--   t.room_id = NEW.room_id AND t.day_of_week = NEW.day_of_week
--   AND NOT (NEW.end_time <= t.start_time OR NEW.start_time >= t.end_time)
--   AND NOT (NEW.week_end < t.week_start OR NEW.week_start > t.week_end)
-- Nếu trùng: SIGNAL SQLSTATE '45000' MESSAGE_TEXT='Schedule conflict: Room is already booked'.
-- VIẾT TRIGGER CỦA BẠN TẠI ĐÂY
-- Q4.3 END $$

DELIMITER ;
