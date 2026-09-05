Câu hỏi 1
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
View trong SQL được mô tả đúng nhất là gì?
Câu hỏi 1Chọn câu trả lời chính xác nhất:

A.
Một cấu trúc tự tạo bảng mới khi truy vấn chạy

B.
Một bản sao dữ liệu dùng để tăng tốc truy vấn

C.
Một bảng ảo được tạo ra từ câu truy vấn SELECT

D.
Một bảng vật lý lưu dữ liệu giống bảng gốc
Phản hồi
The correct answer is: Một bảng ảo được tạo ra từ câu truy vấn SELECT
Câu hỏi 2
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Tại sao View có Aggregation không thể cập nhật được?
Câu hỏi 2Chọn câu trả lời chính xác nhất:

A.
Vì aggregation yêu cầu dữ liệu bất biến

B.
Vì aggregation cần dữ liệu từ nhiều bảng phức tạp

C.
Vì dữ liệu tổng hợp không ánh xạ xuống từng bản ghi

D.
Vì hệ quản trị cấm cập nhật dữ liệu tổng hợp
Phản hồi
The correct answer is: Vì dữ liệu tổng hợp không ánh xạ xuống từng bản ghi
Câu hỏi 3
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
DISTINCT trong View ảnh hưởng thế nào đến cập nhật?
Câu hỏi 3Chọn câu trả lời chính xác nhất:

A.
DISTINCT giúp View ổn định hơn và dễ cập nhật

B.
DISTINCT làm mất ánh xạ dòng nên không cập nhật được

C.
DISTINCT giảm số dòng nên cập nhật chính xác hơn

D.
DISTINCT yêu cầu View luôn được cập nhật tự động
Phản hồi
The correct answer is: DISTINCT làm mất ánh xạ dòng nên không cập nhật được
Câu hỏi 4
Sai
Đạt điểm 0,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Biểu thức nào khiến View không thể cập nhật?
Câu hỏi 4Chọn câu trả lời chính xác nhất:

A.
Bộ lọc WHERE dept_name = 'Biology'

B.
Biểu thức như salary * 1.2 trong SELECT

C.
SELECT * lấy toàn bộ cột từ bảng nguồn

D.
Mệnh đề ORDER BY trên một hoặc nhiều cột
Phản hồi
The correct answer is: Biểu thức như salary * 1.2 trong SELECT
Câu hỏi 5
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
View nào dưới đây có thể cập nhật được?
Câu hỏi 5Chọn câu trả lời chính xác nhất:

A.
View có biểu thức thay đổi giá trị của các cột

B.
View từ một bảng, không GROUP BY và không DISTINCT

C.
View có nhiều phép JOIN phức tạp giữa các bảng

D.
View có nhóm dữ liệu và chứa hàm SUM
Phản hồi
The correct answer is: View từ một bảng, không GROUP BY và không DISTINCT
Câu hỏi 6
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Nhận định nào sau đây đúng về bản chất ánh xạ của View?
Câu hỏi 6Chọn câu trả lời chính xác nhất:

A.
Mỗi dòng trong View có thể ánh xạ đến nhiều dòng

B.
Mỗi dòng của View phải ánh xạ được đến đúng một dòng

C.
View tự tạo dòng mới không phụ thuộc bảng nguồn

D.
View không cần ánh xạ dòng nào xuống bảng gốc
Phản hồi
The correct answer is: Mỗi dòng của View phải ánh xạ được đến đúng một dòng
Câu hỏi 7
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một View có biểu thức salary * 1.5 sẽ gây ra vấn đề gì khi cập nhật?
Câu hỏi 7Chọn câu trả lời chính xác nhất:

A.
Người dùng phải cung cấp thêm tham số khi cập nhật

B.
Cột biểu thức tự khớp với giá trị ban đầu của bảng

C.
Hệ thống không biết cập nhật giá trị nào trong bảng gốc

D.
Giá trị tính toán được lưu trực tiếp vào bảng nguồn
Phản hồi
The correct answer is: Hệ thống không biết cập nhật giá trị nào trong bảng gốc
Câu hỏi 8
Sai
Đạt điểm 0,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Tình huống: View lọc giảng viên thuộc "Biology". UPDATE salary nhưng giữ dept_name nguyên. Điều gì xảy ra?
Câu hỏi 8Chọn câu trả lời chính xác nhất:

A.
UPDATE chỉ áp dụng cho bảng tạm

B.
Bản ghi bị ẩn khỏi View sau khi cập nhật

C.
UPDATE bị từ chối vì không hợp lệ với View

D.
Bản ghi được cập nhật và vẫn nằm trong View
Phản hồi
The correct answer is: Bản ghi được cập nhật và vẫn nằm trong View
Câu hỏi 9
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi UPDATE salary qua View chỉ chọn name và salary, điều gì quyết định việc cập nhật thành công?
Câu hỏi 9Chọn câu trả lời chính xác nhất:

A.
Cột được chỉnh sửa phải ánh xạ về bảng nguồn

B.
Bảng gốc phải có ít nhất 3 thuộc tính

C.
Giá trị mới phải thay đổi trên 10%

D.
Cột được chỉnh sửa phải là biểu thức tính toán
Phản hồi
The correct answer is: Cột được chỉnh sửa phải ánh xạ về bảng nguồn
Câu hỏi 10
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
View tham chiếu nhiều bảng bằng JOIN có đặc điểm gì?
Câu hỏi 10Chọn câu trả lời chính xác nhất:

A.
Chỉ cập nhật được khi JOIN là tự nhiên

B.
Luôn cập nhật được vì JOIN làm rõ nguồn dữ liệu

C.
Chỉ cập nhật được khi bảng không có khóa chính

D.
Thường không cập nhật được do mất ánh xạ dòng
Phản hồi
The correct answer is: Thường không cập nhật được do mất ánh xạ dòng
Câu hỏi 11
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi SELECT từ View có điều kiện dept_name = 'Biology', DBMS làm gì?
Câu hỏi 11Chọn câu trả lời chính xác nhất:

A.
Chạy lại truy vấn gốc với điều kiện Biology

B.
Thay đổi cấu trúc bảng instructor

C.
Tạo bảng sao chép mới rồi lọc dữ liệu

D.
Lấy dữ liệu từ bảng tạm đã sinh sẵn
Phản hồi
The correct answer is: Chạy lại truy vấn gốc với điều kiện Biology
Câu hỏi 12
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Câu lệnh nào được dùng để định nghĩa một View trong SQL?
Câu hỏi 12Chọn câu trả lời chính xác nhất:

A.
INIT VIEW tên_view USING truy_vấn

B.
FORM VIEW tên_view WITH truy_vấn

C.
CREATE VIEW tên_view AS truy_vấn

D.
DEFINE VIEW tên_view AS truy_vấn
Phản hồi
The correct answer is: CREATE VIEW tên_view AS truy_vấn
Câu hỏi 13
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Điều kiện nào KHÔNG ảnh hưởng đến khả năng cập nhật View?
Câu hỏi 13Chọn câu trả lời chính xác nhất:

A.
View có DISTINCT trong truy vấn

B.
View dùng GROUP BY để gom nhóm

C.
View chứa biểu thức tính toán

D.
View có một WHERE đơn giản
Phản hồi
The correct answer is: View có một WHERE đơn giản
Câu hỏi 14
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Đặc điểm chính của View theo video là gì?
Câu hỏi 14Chọn câu trả lời chính xác nhất:

A.
View không lưu dữ liệu mà chỉ lưu câu truy vấn

B.
View cho phép tạo dữ liệu mới không phụ thuộc bảng

C.
View luôn được lưu trữ cùng dữ liệu bảng gốc

D.
View có thể cập nhật độc lập với bảng nguồn
Phản hồi
The correct answer is: View không lưu dữ liệu mà chỉ lưu câu truy vấn
Câu hỏi 15
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một lợi ích quan trọng của View được nhắc đến trong video là gì?
Câu hỏi 15Chọn câu trả lời chính xác nhất:

A.
Cho phép sửa cấu trúc bảng mà không ảnh hưởng người dùng

B.
Hỗ trợ tạo index tự động để tăng tốc độ truy vấn

C.
Ghi log tất cả hoạt động của người dùng trên bảng nguồn

D.
Che giấu một phần dữ liệu để bảo vệ thông tin nhạy cảm
Phản hồi
The correct answer is: Che giấu một phần dữ liệu để bảo vệ thông tin nhạy cảm
Câu hỏi 16
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi người dùng SELECT một View, DBMS thực hiện điều gì?
Câu hỏi 16Chọn câu trả lời chính xác nhất:

A.
Chạy câu truy vấn gốc của View để lấy dữ liệu mới

B.
Lấy dữ liệu từ bản cache đã lưu trên ổ đĩa

C.
Tạo bản sao dữ liệu và lưu vào bộ nhớ ngoài

D.
Sao chép bảng nguồn thành bảng tạm trước khi trả dữ liệu
Phản hồi
The correct answer is: Chạy câu truy vấn gốc của View để lấy dữ liệu mới
Câu hỏi 17
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
“Modification Views” trong video đề cập đến vấn đề gì?
Câu hỏi 17Chọn câu trả lời chính xác nhất:

A.
Tự động đồng bộ dữ liệu giữa nhiều bảng

B.
Cách tối ưu hóa tốc độ hiển thị của View

C.
Tạo bảng vật lý mới dựa trên dữ liệu View

D.
Thực hiện INSERT, UPDATE hoặc DELETE thông qua View
Phản hồi
The correct answer is: Thực hiện INSERT, UPDATE hoặc DELETE thông qua View
Câu hỏi 18
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Vấn đề chính xảy ra khi UPDATE qua View không giới hạn điều kiện là gì?
Câu hỏi 18Chọn câu trả lời chính xác nhất:

A.
Dữ liệu sau cập nhật có thể không còn xuất hiện trong View

B.
View sẽ bị xóa và phải tạo lại từ đầu

C.
Bản ghi bị nhân đôi trong bảng gốc sau khi cập nhật

D.
Toàn bộ các bản ghi khác bị thay đổi theo giá trị mới
Phản hồi
The correct answer is: Dữ liệu sau cập nhật có thể không còn xuất hiện trong View
Câu hỏi 19
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Điều kiện quan trọng nhất để một View có thể cập nhật là gì?
Câu hỏi 19Chọn câu trả lời chính xác nhất:

A.
View phải dựa trên nhiều bảng tham chiếu

B.
View phải có biểu thức tính toán trong SELECT

C.
View phải có mệnh đề ORDER BY ổn định

D.
View chỉ dựa trên một bảng duy nhất
Phản hồi
The correct answer is: View chỉ dựa trên một bảng duy nhất
Câu hỏi 20
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Yếu tố nào làm cho View không thể cập nhật?
Câu hỏi 20Chọn câu trả lời chính xác nhất:

A.
View lọc dữ liệu bằng WHERE đơn giản

B.
View không thực hiện phép tính nào trong SELECT

C.
View chứa GROUP BY hoặc hàm tổng hợp

D.
View hiển thị toàn bộ cột của bảng nguồn
Phản hồi
The correct answer is: View chứa GROUP BY hoặc hàm tổng hợp
