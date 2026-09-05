Câu hỏi 1
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi trigger BEFORE thay đổi giá trị new row, hệ quản trị sẽ
Câu hỏi 1Chọn câu trả lời chính xác nhất:

a.
Ghi nhận giá trị đó tạm thời nhưng không lưu vào bảng.

b.
Bỏ qua giá trị đã sửa và dùng lại giá trị ban đầu.

c.
Ghi nhận song song cả giá trị gốc và giá trị mới.

d.
Ghi nhận giá trị đã thay đổi như giá trị thực tế được lưu.
Phản hồi
Giá trị new row sau khi đã được trigger sửa chính là giá trị cuối cùng mà hệ quản trị dùng để ghi xuống bảng, thay thế cho giá trị do người dùng gửi ban đầu.
The correct answer is: Ghi nhận giá trị đã thay đổi như giá trị thực tế được lưu.
Câu hỏi 2
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi xóa một dòng ở bảng cha với NO ACTION, hệ quản trị sẽ làm gì?
Câu hỏi 2Chọn câu trả lời chính xác nhất:

a.
Vẫn xóa dòng và cập nhật bảng con theo tùy chọn hệ thống.

b.
Tạo một dòng mới để thay thế dòng bị xóa.

c.
Từ chối thao tác vì khóa ngoại đang tồn tại.

d.
Vẫn xóa dòng và đổi khóa ngoại sang giá trị mặc định.
Phản hồi
NO ACTION có nghĩa là không cho phép xóa nếu còn dòng ở bảng con tham chiếu đến. Hệ quản trị sẽ báo lỗi và từ chối thao tác xóa để tránh dữ liệu mồ côi.
The correct answer is: Từ chối thao tác vì khóa ngoại đang tồn tại.
Câu hỏi 3
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Ràng buộc tham chiếu yêu cầu điều gì đối với giá trị khóa ngoại?
Câu hỏi 3Chọn câu trả lời chính xác nhất:

a.
Giá trị phải tồn tại trong dòng được tham chiếu.

b.
Giá trị phải nằm trong khoảng được hệ thống cho phép.

c.
Giá trị phải tuân theo kiểu dữ liệu được đặt ra.

d.
Giá trị phải được cập nhật theo quy tắc mặc định.
Phản hồi
Khóa ngoại phải tham chiếu tới một dòng tồn tại trong bảng cha. Nếu giá trị không tồn tại ở bảng cha thì sẽ vi phạm ràng buộc toàn vẹn tham chiếu.
The correct answer is: Giá trị phải tồn tại trong dòng được tham chiếu.
Câu hỏi 4
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Trigger BEFORE dùng chủ yếu để làm gì?
Câu hỏi 4Chọn câu trả lời chính xác nhất:

a.
Kiểm tra dữ liệu trước khi được ghi vào bảng.

b.
Ghi nội dung log sau khi dữ liệu được lưu.

c.
Thay đổi cấu trúc bảng ngay khi thao tác bắt đầu.

d.
Tạo thêm dòng mới sau khi thao tác hoàn tất.
Phản hồi
Trigger BEFORE chạy trước khi dữ liệu được ghi xuống bảng, nên rất phù hợp để kiểm tra, chuẩn hóa hoặc chỉnh sửa dữ liệu nhằm đảm bảo tính hợp lệ trước khi lưu trữ.
The correct answer is: Kiểm tra dữ liệu trước khi được ghi vào bảng.
Câu hỏi 5
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Cột được tham chiếu trong ràng buộc tham chiếu phải thỏa điều kiện nào?
Câu hỏi 5Chọn câu trả lời chính xác nhất:

a.
Cột đó phải là cột có đơn vị đo nhất quán.

b.
Cột đó phải chứa dữ liệu được gán thủ công.

c.
Cột đó phải giữ nguyên trong suốt vòng đời bảng.

d.
Cột đó phải là khóa chính của bảng cha.
Phản hồi
Để đảm bảo mỗi giá trị khóa ngoại trỏ tới một dòng duy nhất ở bảng cha, cột được tham chiếu thường là khóa chính hoặc khóa duy nhất của bảng cha.
The correct answer is: Cột đó phải là khóa chính của bảng cha.
Câu hỏi 6
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Ý nghĩa của ON DELETE CASCADE là gì?
Câu hỏi 6Chọn câu trả lời chính xác nhất:

a.
Hệ quản trị bỏ qua ràng buộc khi xóa dữ liệu.

b.
Các ràng buộc trong bảng cha bị vô hiệu tạm thời.

c.
Tất cả khóa ngoại chuyển thành NULL.

d.
Bảng con sẽ tự động xóa các dòng liên quan.
Phản hồi
ON DELETE CASCADE quy định rằng khi một dòng ở bảng cha bị xóa, mọi dòng ở bảng con đang tham chiếu đến dòng đó cũng sẽ bị xóa theo, để tránh dữ liệu tham chiếu tới dòng không còn tồn tại.
The correct answer is: Bảng con sẽ tự động xóa các dòng liên quan.
Câu hỏi 7
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một trigger có thể gây lỗi trong trường hợp nào?
Câu hỏi 7Chọn câu trả lời chính xác nhất:

a.
Khi thao tác được thực thi trong khoảng thời gian cao điểm.

b.
Khi giá trị được cập nhật trùng với cấu trúc chỉ mục.

c.
Khi thao tác được thực thi từ một bảng không có chỉ mục.

d.
Khi giá trị mới không thỏa điều kiện xác minh của trigger.
Phản hồi
Trigger thường chứa các điều kiện kiểm tra. Nếu điều kiện không được thỏa, trigger có thể chủ động báo lỗi hoặc vi phạm ràng buộc, khiến câu lệnh gốc không được thực hiện.
The correct answer is: Khi giá trị mới không thỏa điều kiện xác minh của trigger.
Câu hỏi 8
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Việc cập nhật khóa chính ở bảng cha có thể dẫn đến điều gì?
Câu hỏi 8Chọn câu trả lời chính xác nhất:

a.
Khóa ngoại tự chuyển thành giá trị mặc định.

b.
Dữ liệu bảng con được nhân bản để tránh lỗi.

c.
Ràng buộc tham chiếu có thể bị vi phạm.

d.
Hệ quản trị tự tạo một dòng thay thế.
Phản hồi
Nếu thay đổi giá trị khóa chính mà không cập nhật tương ứng các khóa ngoại ở bảng con, các khóa ngoại sẽ trỏ tới giá trị không còn tồn tại, gây vi phạm ràng buộc tham chiếu.
The correct answer is: Ràng buộc tham chiếu có thể bị vi phạm.
Câu hỏi 9
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Trong một thao tác UPDATE cấp dòng, trigger có thể truy cập bao nhiêu loại biến?
Câu hỏi 9Chọn câu trả lời chính xác nhất:

a.
Bốn biến gồm old row, new row, old table và new table.

b.
Hai biến gồm giá trị cũ và giá trị mới của bảng.

c.
Ba biến gồm giá trị mới, giá trị cũ và toàn bộ bảng.

d.
Một biến duy nhất là bản ghi mới được cập nhật.
Phản hồi
Đối với UPDATE cấp dòng, trigger có thể thấy cả giá trị cũ và mới của dòng (old row, new row), đồng thời trong một số hệ quản trị còn có khái niệm bảng cũ và bảng mới (old table, new table) ở mức câu lệnh.
The correct answer is: Bốn biến gồm old row, new row, old table và new table.
Câu hỏi 10
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Trigger đệ quy được hiểu là gì?
Câu hỏi 10Chọn câu trả lời chính xác nhất:

a.
Trigger chỉ thực thi khi hệ quản trị ở trạng thái đặc biệt.

b.
Trigger kích hoạt lại chính nó do thao tác nó tạo ra.

c.
Trigger được sao chép thành nhiều bản khi thao tác lớn.

d.
Trigger chạy tuần tự theo thứ tự khai báo ban đầu.
Phản hồi
Trigger đệ quy là trường hợp trigger thực hiện một thao tác (như INSERT, UPDATE, DELETE) trên chính bảng có trigger, khiến trigger đó được kích hoạt nhiều lần theo chuỗi.
The correct answer is: Trigger kích hoạt lại chính nó do thao tác nó tạo ra.
Câu hỏi 11
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Trigger AFTER có đặc điểm nào sau đây?
Câu hỏi 11Chọn câu trả lời chính xác nhất:

a.
Chỉ chạy khi cấu trúc bảng thay đổi trong hệ thống.

b.
Tự động vô hiệu khi thao tác liên quan đến khóa chính.

c.
Chỉ thực thi sau khi thao tác chính đã hoàn thành.

d.
Có thể chỉnh sửa dữ liệu trước khi ghi xuống bảng.
Phản hồi
Trigger AFTER được kích hoạt sau khi thao tác trên bảng đã hoàn tất, nên thường dùng để ghi log, cập nhật bảng phụ hoặc các xử lý hậu kiểm, không dùng để sửa dữ liệu trước khi lưu.
The correct answer is: Chỉ thực thi sau khi thao tác chính đã hoàn thành.
Câu hỏi 12
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi một trigger trong phiên thực thi gây lỗi, điều gì sẽ xảy ra?
Câu hỏi 12Chọn câu trả lời chính xác nhất:

a.
Thao tác gốc bị hủy và dữ liệu quay về trạng thái trước đó.

b.
Giá trị mới được ghi nhưng không kiểm tra thêm ràng buộc.

c.
Chỉ trigger đó dừng, các trigger khác vẫn tiếp tục chạy.

d.
Toàn bộ phiên trigger tiếp tục nhưng bỏ qua lỗi vừa gặp.
Phản hồi
Trong hầu hết hệ quản trị, nếu trigger gây lỗi thì cả thao tác gốc (INSERT, UPDATE, DELETE) sẽ bị hủy, giao dịch quay về trạng thái trước đó để đảm bảo toàn vẹn dữ liệu.
The correct answer is: Thao tác gốc bị hủy và dữ liệu quay về trạng thái trước đó.
Câu hỏi 13
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi một câu lệnh UPDATE tác động lên nhiều dòng, trigger sẽ
Câu hỏi 13Chọn câu trả lời chính xác nhất:

a.
Chạy một phần tùy thuộc vào điều kiện của transaction.

b.
Chỉ chạy một lần cho toàn bộ câu lệnh được kích hoạt.

c.
Chạy lại nhiều lần tương ứng theo từng dòng bị cập nhật.

d.
Không chạy cho các dòng không có thay đổi về khóa chính.
Phản hồi
Trong mô hình FOR EACH ROW, mỗi dòng bị ảnh hưởng bởi câu lệnh UPDATE sẽ kích hoạt trigger một lần, nên tổng số lần thực thi trigger bằng số dòng được cập nhật.
The correct answer is: Chạy lại nhiều lần tương ứng theo từng dòng bị cập nhật.
Câu hỏi 14
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Vì sao ON DELETE CASCADE có thể tạo chuỗi xóa lan truyền?
Câu hỏi 14Chọn câu trả lời chính xác nhất:

a.
Vì trigger lặp lại vô hạn khi có thay đổi.

b.
Vì hệ quản trị tự động bỏ qua mọi ràng buộc.

c.
Vì mọi khóa ngoại đều được thay đổi đồng loạt.

d.
Vì bảng con có thể tiếp tục tham chiếu sang bảng khác.
Phản hồi
Nếu một bảng con lại đóng vai trò bảng cha của bảng khác, việc xóa một dòng gốc có thể kéo theo xóa dòng ở nhiều bảng liên tiếp, tạo thành chuỗi xóa lan truyền qua các quan hệ khóa ngoại.
The correct answer is: Vì bảng con có thể tiếp tục tham chiếu sang bảng khác.
Câu hỏi 15
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một trigger UPDATE kích hoạt một trigger khác, và cả hai đều bật recursive triggers. Điều gì có thể xảy ra?
Câu hỏi 15Chọn câu trả lời chính xác nhất:

a.
Chuỗi trigger lặp nhiều lần cho đến khi hệ thống dừng.

b.
Hệ quản trị tự động bỏ qua mọi trigger lặp tiếp theo.

c.
Trigger chỉ chạy nếu người dùng cấp quyền đặc biệt.

d.
Trigger thứ hai chạy một lần rồi vô hiệu hóa trigger đầu.
Phản hồi
Nếu mỗi trigger lại thực hiện thao tác tiếp tục kích hoạt trigger kia, chuỗi gọi lẫn nhau có thể lặp lại nhiều lần cho đến khi bị giới hạn độ sâu hoặc gây lỗi, nên phải thiết kế rất cẩn thận.
The correct answer is: Chuỗi trigger lặp nhiều lần cho đến khi hệ thống dừng.
Câu hỏi 16
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi recursive trigger được bật và trigger tự kích hoạt lại chính nó, điều gì có thể xảy ra?
Câu hỏi 16Chọn câu trả lời chính xác nhất:

a.
Trigger được hệ thống ghi nhận nhưng không được phép thực thi tiếp tục.

b.
Trigger chuyển thành chế độ kiểm tra tĩnh để tránh vòng lặp.

c.
Trigger chỉ chạy lại một lần rồi dừng theo quy tắc mặc định.

d.
Trigger tiếp tục thực thi lặp lại cho đến khi hệ quản trị chặn chu kỳ.
Phản hồi
Nếu trigger thực hiện thao tác tiếp tục kích hoạt chính nó và recursive trigger được cho phép, chuỗi thực thi có thể lặp lại nhiều lần cho đến khi bị hệ quản trị chặn bởi giới hạn hoặc lỗi.
The correct answer is: Trigger tiếp tục thực thi lặp lại cho đến khi hệ quản trị chặn chu kỳ.
Câu hỏi 17
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một trigger BEFORE UPDATE thay đổi giá trị vượt ngưỡng thành giá trị hợp lệ. Điều gì xảy ra?
Câu hỏi 17Chọn câu trả lời chính xác nhất:

a.
Giá trị được cập nhật trực tiếp mà không có thay đổi.

b.
Trigger thay đổi giá trị new row trước khi lưu xuống bảng.

c.
Trigger bị bỏ qua vì thao tác không vi phạm chuẩn SQL.

d.
Trigger chỉ đưa ra cảnh báo nhưng vẫn giữ nguyên giá trị.
Phản hồi
Vì trigger chạy trước khi lệnh UPDATE hoàn tất, nó có thể ghi đè giá trị new row. Khi đó, giá trị lưu xuống bảng chính là giá trị đã được trigger chỉnh sửa lại.
The correct answer is: Trigger thay đổi giá trị new row trước khi lưu xuống bảng.
Câu hỏi 18
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Một trigger AFTER INSERT ghi nhật ký mỗi khi có dòng mới. Nếu một câu lệnh INSERT tạo 10 dòng, trigger chạy bao nhiêu lần?
Câu hỏi 18Chọn câu trả lời chính xác nhất:

a.
Trigger chạy mười lần tương ứng với mười dòng mới.

b.
Trigger không chạy vì AFTER không hỗ trợ nhiều dòng.

c.
Trigger chạy một lần cho toàn bộ câu lệnh INSERT.

d.
Trigger chạy đúng năm lần theo cấu hình mặc định.
Phản hồi
Với trigger dạng FOR EACH ROW, mỗi dòng được chèn sẽ kích hoạt trigger một lần, nên nếu INSERT thêm 10 dòng thì trigger được kích hoạt 10 lần.
The correct answer is: Trigger chạy mười lần tương ứng với mười dòng mới.
Câu hỏi 19
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi INSERT vào bảng con, hệ quản trị kiểm tra điều gì?
Câu hỏi 19Chọn câu trả lời chính xác nhất:

a.
Khóa ngoại có khớp với giá trị hợp lệ trong bảng cha.

b.
Khóa ngoại có tuân theo thứ tự sắp xếp của toàn bảng hay không.

c.
Khóa ngoại có nằm trong chỉ mục hỗ trợ truy vấn hay không.

d.
Khóa ngoại có bằng giá trị mặc định hay không.
Phản hồi
Mỗi giá trị khóa ngoại chèn vào bảng con phải khớp với một giá trị khóa chính (hoặc khóa được tham chiếu) trong bảng cha. Nếu không khớp, INSERT sẽ vi phạm ràng buộc tham chiếu.
The correct answer is: Khóa ngoại có khớp với giá trị hợp lệ trong bảng cha.
Câu hỏi 20
Đúng
Đạt điểm 1,00 trên 1,00
Đặt cờ
Đoạn văn câu hỏi
Khi có nhiều trigger cùng loại, hệ quản trị sẽ
Câu hỏi 20Chọn câu trả lời chính xác nhất:

a.
Chặn tất cả trigger và yêu cầu sắp xếp thủ công.

b.
Thực thi chúng theo một thứ tự do hệ thống xác định.

c.
Chạy trigger có độ ưu tiên thấp nhất trước tiên.

d.
Tự động gộp chúng thành một trigger duy nhất.
Phản hồi
Nếu có nhiều trigger cùng loại trên cùng một bảng và sự kiện, hệ quản trị sẽ thực thi chúng theo thứ tự nội bộ (hoặc cấu hình), chứ không tự gộp hay tự động chặn tất cả.
The correct answer is: Thực thi chúng theo một thứ tự do hệ thống xác định.