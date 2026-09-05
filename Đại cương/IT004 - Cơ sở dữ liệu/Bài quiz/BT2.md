Câu hỏi 1
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Mục tiêu chính của Isolation trong ACID là gì?
Câu hỏi 1Chọn câu trả lời chính xác nhất:

a.
Tự động sắp xếp thứ tự giao dịch.

b.
Giúp tối ưu hóa lưu trữ dữ liệu.

c.
Giảm thời gian khóa bảng.

d.
Đảm bảo các transaction thực thi độc lập.
Phản hồi
The correct answer is: Đảm bảo các transaction thực thi độc lập.
Câu hỏi 2
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi nào Lost Update xảy ra?
Câu hỏi 2Chọn câu trả lời chính xác nhất:

a.
Hai transaction ghi đè nhau.

b.
Đọc dữ liệu chưa commit.

c.
Thấy thêm dòng mới.

d.
Giá trị thay đổi hai lần đọc.
Phản hồi
The correct answer is: Hai transaction ghi đè nhau.
Câu hỏi 3
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Mức Isolation ngăn Dirty, Non-repeatable và Phantom:
Câu hỏi 3Chọn câu trả lời chính xác nhất:

a.
Repeatable Read.

b.
Read Committed.

c.
Serializable.

d.
Read Uncommitted.
Phản hồi
The correct answer is: Serializable.
Câu hỏi 4
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Serializable mô tả:
Câu hỏi 4Chọn câu trả lời chính xác nhất:

a.
Giao dịch luôn gặp deadlock khi nạp dữ liệu nặng.

b.
Transaction chạy theo thứ tự tuần tự về mặt logic.

c.
Bảng bị khóa toàn bộ trong mỗi lần ghi.

d.
Dữ liệu bị flush ngay lập tức khi thay đổi.
Phản hồi
The correct answer is: Transaction chạy theo thứ tự tuần tự về mặt logic.
Câu hỏi 5
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Scenario Lost Update:
Câu hỏi 5Chọn câu trả lời chính xác nhất:

a.
Hai transaction ghi đè lên nhau không kiểm tra xung đột.

b.
Bản ghi bị xóa do thiếu khóa.

c.
Dữ liệu được đọc từ snapshot lỗi.

d.
Log bị ghi chậm hơn dữ liệu thực.
Phản hồi
The correct answer is: Hai transaction ghi đè lên nhau không kiểm tra xung đột.
Câu hỏi 6
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi nào Phantom Read xảy ra nhiều nhất?
Câu hỏi 6Chọn câu trả lời chính xác nhất:

a.
Khi truy vấn theo điều kiện phạm vi.

b.
Khi thực hiện phép JOIN.

c.
Khi sử dụng khóa ngoại.

d.
Khi cập nhật hàng theo chỉ mục.
Phản hồi
The correct answer is: Khi truy vấn theo điều kiện phạm vi.
Câu hỏi 7
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Mục tiêu chính của Serializable:
Câu hỏi 7Chọn câu trả lời chính xác nhất:

a.
Đảm bảo mỗi lần đọc đều dùng snapshot.

b.
Đảm bảo thực thi logic giống tuần tự.

c.
Đảm bảo mọi đọc đều dùng khóa chia sẻ.

d.
Tăng tốc độ ghi bằng cách gom nhóm log.
Phản hồi
The correct answer is: Đảm bảo thực thi logic giống tuần tự.
Câu hỏi 8
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi nào Read Committed gây vấn đề?
Câu hỏi 8Chọn câu trả lời chính xác nhất:

a.
Khi dữ liệu thay đổi giữa 2 lần quét.

b.
Khi cần đọc dữ liệu chưa commit.

c.
Khi dữ liệu bị khóa bảng.

d.
Khi không thể thực thi JOIN.
Phản hồi
The correct answer is: Khi dữ liệu thay đổi giữa 2 lần quét.
Câu hỏi 9
Sai
Đạt điểm 0,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Scenario: tổng số đơn hàng thay đổi giữa hai lần đọc.
Câu hỏi 9Chọn câu trả lời chính xác nhất:

a.
Read Committed.

b.
Serializable.

c.
Repeatable Read.

d.
Static Query Mode.
Phản hồi
The correct answer is: Read Committed.
Câu hỏi 10
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Muốn tránh thay đổi giá trị đã đọc nhưng không quan tâm Phantom:
Câu hỏi 10Chọn câu trả lời chính xác nhất:

a.
Repeatable Read.

b.
Read Anywhere.

c.
Read Committed.

d.
Uncommitted Scan.
Phản hồi
The correct answer is: Repeatable Read.
Câu hỏi 11
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Anomaly khi dùng dữ liệu từ transaction bị rollback:
Câu hỏi 11Chọn câu trả lời chính xác nhất:

a.
Non-repeatable.

b.
Dirty Read.

c.
Phantom.

d.
Partial Aggregation.
Phản hồi
The correct answer is: Dirty Read.
Câu hỏi 12
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Dirty Read là gì?
Câu hỏi 12Chọn câu trả lời chính xác nhất:

a.
Thay đổi giá trị bị rollback.

b.
Xóa bản ghi khi chưa có khóa.

c.
Đọc dữ liệu chưa commit.

d.
Ghi dữ liệu không tạo log.
Phản hồi
The correct answer is: Đọc dữ liệu chưa commit.
Câu hỏi 13
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Isolation phù hợp cho truy vấn phân tích tuyệt đối:
Câu hỏi 13Chọn câu trả lời chính xác nhất:

a.
Read Committed.

b.
Read Snapshot.

c.
Serializable.

d.
Mixed View Read.
Phản hồi
The correct answer is: Serializable.
Câu hỏi 14
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Isolation Level thấp nhất trong chuẩn SQL là:
Câu hỏi 14Chọn câu trả lời chính xác nhất:

a.
Repeatable Read.

b.
Serializable.

c.
Read Uncommitted.

d.
Read Committed.
Phản hồi
The correct answer is: Read Uncommitted.
Câu hỏi 15
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Non-repeatable Read xảy ra khi:
Câu hỏi 15Chọn câu trả lời chính xác nhất:

a.
Một giá trị thay đổi giữa hai lần đọc.

b.
Transaction bị tạm dừng do lỗi mạng.

c.
Bản ghi bị xóa nhưng khóa còn giữ.

d.
Chỉ mục được tạo lại khi đang đọc.
Phản hồi
The correct answer is: Một giá trị thay đổi giữa hai lần đọc.
Câu hỏi 16
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Read Uncommitted cho phép:
Câu hỏi 16Chọn câu trả lời chính xác nhất:

a.
Đọc dữ liệu chưa commit.

b.
Tạo snapshot mới cho mỗi lần đọc.

c.
Ghi dữ liệu không kiểm tra khóa.

d.
Phân quyền truy cập theo phạm vi.
Phản hồi
The correct answer is: Đọc dữ liệu chưa commit.
Câu hỏi 17
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Read Committed ngăn chặn anomaly nào?
Câu hỏi 17Chọn câu trả lời chính xác nhất:

a.
Phantom Read.

b.
Dirty Read.

c.
Lost Update.

d.
Write Skew.
Phản hồi
The correct answer is: Dirty Read.
Câu hỏi 18
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Scenario: T1 đọc danh sách khách hàng, T2 xóa một dòng, T1 đọc lại và thấy thiếu.
Câu hỏi 18Chọn câu trả lời chính xác nhất:

a.
Dirty Read.

b.
Non-repeatable Read.

c.
Phantom-like Removal.

d.
Lost Update.
Phản hồi
The correct answer is: Non-repeatable Read.
Câu hỏi 19
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
T1 đọc tổng số dòng, T2 thêm dòng mới, T1 đọc lại và thấy tăng.
Câu hỏi 19Chọn câu trả lời chính xác nhất:

a.
Phantom Read.

b.
Dirty Read.

c.
Update Drift.

d.
Read Conflict.
Phản hồi
The correct answer is: Phantom Read.
Câu hỏi 20
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Scenario: T1 cập nhật nhưng chưa commit, T2 đọc giá trị này và T1 rollback.
Câu hỏi 20Chọn câu trả lời chính xác nhất:

a.
Lost Update.

b.
Phantom Read.

c.
Dirty Read.

d.
Non-repeatable Read.
Phản hồi
The correct answer is: Dirty Read.