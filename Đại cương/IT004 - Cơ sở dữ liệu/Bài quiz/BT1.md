Câu hỏi 1
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Sau khi commit, dữ liệu được lưu ở đâu để đảm bảo bền vững?
Câu hỏi 1Chọn câu trả lời chính xác nhất:

a.
Trong vùng bộ nhớ đệm tạm thời để phục vụ truy vấn sau.

b.
Trên ổ đĩa vật lý hoặc hệ thống lưu trữ lâu dài của DBMS.

c.
Trên thiết bị ngoại vi chưa được đồng bộ với hệ thống chính.

d.
Trong file log cục bộ có thể bị xóa sau mỗi phiên.
Phản hồi
The correct answer is: Trên ổ đĩa vật lý hoặc hệ thống lưu trữ lâu dài của DBMS.
Câu hỏi 2
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Mục tiêu chính của rollback là gì?
Câu hỏi 2Chọn câu trả lời chính xác nhất:

a.
Sao lưu dữ liệu sang môi trường kiểm thử để phân tích.

b.
Tăng hiệu suất bằng cách loại bỏ transaction không cần thiết.

c.
Ghi lại toàn bộ lịch sử thao tác để phục vụ báo cáo.

d.
Bảo đảm dữ liệu an toàn và toàn vẹn khi transaction bị lỗi.
Phản hồi
The correct answer is: Bảo đảm dữ liệu an toàn và toàn vẹn khi transaction bị lỗi.
Câu hỏi 3
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Rollback giúp đảm bảo tính chất nào trong ACID?
Câu hỏi 3Chọn câu trả lời chính xác nhất:

a.
Atomicity – cho phép hoàn tác toàn bộ nếu transaction không hoàn thành.

b.
Isolation – tách biệt các transaction đang xử lý song song.

c.
Durability – ghi vĩnh viễn kết quả commit vào đĩa cứng.

d.
Consistency – kiểm tra lại dữ liệu sau mỗi thao tác ghi.
Phản hồi
The correct answer is: Atomicity – cho phép hoàn tác toàn bộ nếu transaction không hoàn thành.
Câu hỏi 4
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Transaction nhằm giải quyết vấn đề nào chính?
Câu hỏi 4Chọn câu trả lời chính xác nhất:

a.
Cải thiện giao diện người dùng và tối ưu hóa tốc độ front-end.

b.
Nâng cao tốc độ phản hồi cho các truy vấn phức tạp trong môi trường mạng.

c.
Quản lý truy cập đồng thời của nhiều user và giúp phục hồi khi hệ thống gặp sự cố.

d.
Tự động phân mảnh dữ liệu và cân bằng tải giữa nhiều vùng lưu trữ khác nhau.
Phản hồi
The correct answer is: Quản lý truy cập đồng thời của nhiều user và giúp phục hồi khi hệ thống gặp sự cố.
Câu hỏi 5
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi hai transaction cùng sửa một bản ghi, DBMS sẽ làm gì?
Câu hỏi 5Chọn câu trả lời chính xác nhất:

a.
Ghi đồng thời cả hai thay đổi và chọn ngẫu nhiên một kết quả cuối.

b.
Xóa dữ liệu cũ và thay bằng bản ghi mới của transaction sau.

c.
Sao chép dữ liệu cho mỗi người và hợp nhất sau khi hoàn tất.

d.
Chặn một transaction cho đến khi transaction kia hoàn tất ghi.
Phản hồi
The correct answer is: Chặn một transaction cho đến khi transaction kia hoàn tất ghi.
Câu hỏi 6
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Durability đảm bảo điều gì khi transaction commit?
Câu hỏi 6Chọn câu trả lời chính xác nhất:

a.
Log chỉ được lưu tạm và xóa khi phiên kết thúc.

b.
Hệ thống lưu một bản sao trong RAM chờ xác nhận từ quản trị.

c.
Dữ liệu chỉ hiển thị sau khi admin kiểm tra thủ công.

d.
Thay đổi được ghi vĩnh viễn và tồn tại kể cả khi hệ thống gặp sự cố.
Phản hồi
The correct answer is: Thay đổi được ghi vĩnh viễn và tồn tại kể cả khi hệ thống gặp sự cố.
Câu hỏi 7
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Consistency đảm bảo điều gì?
Câu hỏi 7Chọn câu trả lời chính xác nhất:

a.
Các bản sao của dữ liệu trên nhiều máy chủ luôn đồng bộ chính xác theo thời gian thực.

b.
Mọi lần truy vấn đều trả về dữ liệu đã được xác thực và lọc kỹ lưỡng.

c.
Hệ thống luôn sao lưu định kỳ để tránh mất dữ liệu.

d.
Cơ sở dữ liệu thỏa mãn các ràng buộc toàn vẹn trước và sau transaction.
Phản hồi
The correct answer is: Cơ sở dữ liệu thỏa mãn các ràng buộc toàn vẹn trước và sau transaction.
Câu hỏi 8
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Mục tiêu của cơ chế khóa (locking) là gì?
Câu hỏi 8Chọn câu trả lời chính xác nhất:

a.
Dọn dẹp các bản ghi trùng lặp để giảm kích thước cơ sở dữ liệu.

b.
Ghi log chi tiết mọi thao tác để phân tích hoạt động người dùng.

c.
Tăng tốc độ truy vấn bằng cách khóa toàn bộ bảng trong suốt phiên.

d.
Ngăn ngừa xung đột và đảm bảo dữ liệu không bị thay đổi sai lệch.
Phản hồi
The correct answer is: Ngăn ngừa xung đột và đảm bảo dữ liệu không bị thay đổi sai lệch.
Câu hỏi 9
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
DBMS dùng cơ chế nào để điều phối truy cập khi có nhiều người cùng thao tác?
Câu hỏi 9Chọn câu trả lời chính xác nhất:

a.
Tạo thêm bản sao cho từng người dùng và hợp nhất tự động sau khi hoàn tất.

b.
Cơ chế khóa (locking) để kiểm soát quyền đọc/ghi dữ liệu.

c.
Tự động chia bảng và phân vùng khi có nhiều truy vấn đồng thời.

d.
Áp dụng thuật toán nén và mã hóa để giảm xung đột truy cập.
Phản hồi
The correct answer is: Cơ chế khóa (locking) để kiểm soát quyền đọc/ghi dữ liệu.
Câu hỏi 10
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Isolation nghĩa là gì?
Câu hỏi 10Chọn câu trả lời chính xác nhất:

a.
Toàn bộ database sẽ bị khóa khi một transaction bắt đầu.

b.
Hệ thống chỉ cho phép một người dùng truy cập cơ sở dữ liệu tại cùng thời điểm.

c.
Mọi thao tác ghi đều chuyển sang vùng lưu trữ riêng biệt để tránh xung đột.

d.
Các transaction được thực thi tách biệt, tạo kết quả như khi chạy tuần tự.
Phản hồi
The correct answer is: Các transaction được thực thi tách biệt, tạo kết quả như khi chạy tuần tự.
Câu hỏi 11
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi nhiều người cùng thao tác, Transaction giúp điều gì?
Câu hỏi 11Chọn câu trả lời chính xác nhất:

a.
Ghi lại nhật ký chi tiết mọi hành động của người dùng để phục vụ kiểm tra sau.

b.
Tự động sao lưu toàn bộ dữ liệu theo chu kỳ để phục hồi nhanh.

c.
Duy trì tính nhất quán của dữ liệu và tránh xung đột thao tác.

d.
Tăng băng thông kết nối giữa client và server để giảm độ trễ khi truy vấn.
Phản hồi
The correct answer is: Duy trì tính nhất quán của dữ liệu và tránh xung đột thao tác.
Câu hỏi 12
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Transaction trong cơ sở dữ liệu là gì?
Câu hỏi 12Chọn câu trả lời chính xác nhất:

a.
Một khối các câu lệnh SQL rời rạc được chạy độc lập với nhau mỗi lần.

b.
Một bảng đặc thù dùng tạm cho mục đích kiểm thử và lưu trữ trung gian.

c.
Một tiến trình đơn lẻ chỉ có chức năng đọc thông tin mà không thay đổi gì.

d.
Một đơn vị công việc logic gồm nhiều thao tác liên quan đến việc đọc và ghi dữ liệu.
Phản hồi
The correct answer is: Một đơn vị công việc logic gồm nhiều thao tác liên quan đến việc đọc và ghi dữ liệu.
Câu hỏi 13
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Ý nghĩa của serializability là gì?
Câu hỏi 13Chọn câu trả lời chính xác nhất:

a.
Các transaction song song cho kết quả giống như khi chạy tuần tự.

b.
Hệ thống chỉ cho phép một transaction được chạy trong mỗi chu kỳ CPU.

c.
Transaction được xếp hàng chờ xử lý theo thời gian gửi yêu cầu.

d.
Các transaction lỗi được chạy lại tự động đến khi thành công.
Phản hồi
The correct answer is: Các transaction song song cho kết quả giống như khi chạy tuần tự.
Câu hỏi 14
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Dữ liệu thực tế trong DBMS thường được lưu ở đâu?
Câu hỏi 14Chọn câu trả lời chính xác nhất:

a.
Trong ổ đĩa vật lý hoặc hệ thống lưu trữ do DBMS quản lý.

b.
Trong hệ thống lưu trữ đám mây không trực tiếp kiểm soát bởi DBMS.

c.
Trong bộ nhớ CPU cache nhằm đạt hiệu suất cao nhất khi đọc dữ liệu.

d.
Trong vùng nhớ đệm tạm thời (cache) để tăng tốc truy vấn ngắn hạn.
Phản hồi
The correct answer is: Trong ổ đĩa vật lý hoặc hệ thống lưu trữ do DBMS quản lý.
Câu hỏi 15
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Hai người cùng cập nhật cùng dữ liệu minh họa cho điều gì?
Câu hỏi 15Chọn câu trả lời chính xác nhất:

a.
Lỗi logic trong ứng dụng dẫn tới việc ghi sai dữ liệu.

b.
Cạnh tranh truy cập giữa các transaction chạy đồng thời.

c.
Mất dữ liệu do lỗi phần cứng.

d.
Hiệu suất giảm do thiếu chỉ mục cho truy vấn.
Phản hồi
The correct answer is: Cạnh tranh truy cập giữa các transaction chạy đồng thời.
Câu hỏi 16
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Rollback còn được gọi là gì?
Câu hỏi 16Chọn câu trả lời chính xác nhất:

a.
Cancel command – huỷ yêu cầu nhưng giữ tạm dữ liệu.

b.
Undo transaction – hoàn tác các thay đổi trước đó.

c.
Restore session – khôi phục lại toàn bộ phiên làm việc.

d.
Replay transaction – chạy lại toàn bộ lệnh đã thực hiện.
Phản hồi
The correct answer is: Undo transaction – hoàn tác các thay đổi trước đó.
Câu hỏi 17
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Ai có thể khởi tạo rollback?
Câu hỏi 17Chọn câu trả lời chính xác nhất:

a.
Hệ thống sao lưu tự động khi phát hiện sự cố phần cứng.

b.
Quản trị viên chạy lệnh đặc biệt từ terminal.

c.
Người dùng hoặc ứng dụng khi muốn hủy thao tác.

d.
Tiến trình nền của máy chủ khi tải hệ thống cao.
Phản hồi
The correct answer is: Người dùng hoặc ứng dụng khi muốn hủy thao tác.
Câu hỏi 18
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Sau rollback, dữ liệu trở về trạng thái nào?
Câu hỏi 18Chọn câu trả lời chính xác nhất:

a.
Trạng thái trung gian giữa hai lần commit gần nhất.

b.
Trạng thái chính xác trước khi transaction bắt đầu.

c.
Trạng thái chờ xác nhận từ hệ thống sao lưu.

d.
Trạng thái do người dùng lựa chọn trong tùy chỉnh khôi phục.
Phản hồi
The correct answer is: Trạng thái chính xác trước khi transaction bắt đầu.
Câu hỏi 19
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Chữ A trong ACID là viết tắt của gì?
Câu hỏi 19Chọn câu trả lời chính xác nhất:

a.
Autonomy – transaction vận hành độc lập với các thành phần khác.

b.
Adaptability – khả năng hệ thống thích ứng khi schema thay đổi.

c.
Accessibility – đảm bảo dữ liệu luôn có thể truy cập được khi cần.

d.
Atomicity – thực hiện toàn bộ hoặc không thực hiện gì cả.
Phản hồi
The correct answer is: Atomicity – thực hiện toàn bộ hoặc không thực hiện gì cả.
Câu hỏi 20
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi transaction gặp lỗi, hệ thống sẽ làm gì?
Câu hỏi 20Chọn câu trả lời chính xác nhất:

a.
Tạm lưu thay đổi và tiếp tục khi hệ thống ổn định.

b.
Giữ nguyên phần dữ liệu hợp lệ và bỏ phần sai.

c.
Hoàn tác toàn bộ thay đổi để trở về trạng thái ban đầu.

d.
Ghi log lỗi để quản trị viên xử lý thủ công sau.
Phản hồi
The correct answer is: Hoàn tác toàn bộ thay đổi để trở về trạng thái ban đầu.
