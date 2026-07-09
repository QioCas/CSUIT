[Từ 7h45]
- Đèn đều tắt hết thì tín hiệu là gì?
- Đèn đỏ có được quẹt phải ko.
- Cả 3 đèn sáng hết thì sao.
dẫn nhập

Input biển báo, hỏi biển báo gì.
Bài cơ bản? Cho biển báo giao thông, và tôi chạy xe abc thì mình có được chạy ko, chạy tốc độ bao nhiêu bla bla.

Làm đồ án thì hướng ứng dụng, hướng thực tế nhiều hơn. 
Mình sẽ biết cách kết hợp bài toán để giải quyết bài toán phức tạp hơn, tính học thuật cao hoặc tính ứng dụng cao hơn.

Nhận xét được số trên tín hiệu hay ko?

Không cần suy nghĩ bài toán quá phức tạp. 
Có thể suy nghĩ những bài toán đơn giản nhưng mang tính thực tế. 

Đèn giao thông là ở đâu vì mỗi đèn mỗi khác. Dataset đèn ở đâu. Đèn giao thông ở mỗi chỗ khác nhau.

Xét những trường hợp ngoại lệ. Những đèn phụ.

Đặc trưng màu sắc. 

Các ý tưởng xuất phát từ sv.

## Histogram 
là lĩnh vực thống kê.

số bin. 

Gray [0,255]
RGB [0-255,0-255,0-255]
HSV [0-179,0-255,0-255]
...

approx thành số bin, để giảm số chiều.

Thứ nhất, khi báo cáo thầy sẽ hỏi
Đặc trưng màu sắc. 3 kênh màu. 
Sử dụng histogram 3 kênh màu, concat với nhau. 

feature đặc trưng là 256+256+256=788
Độ dài vector đặc trưng là bao nhiêu. phải để ý size.

Tổ hợp r tính thì có độ chính xác cao hơn.

Tại sao histogram bị hạn chế khi nội dung khác nhau nhưng vẫn bị dính giống nhau 
do ko sử dụng yếu tố không gian. 

Toàn cục và cục bộ. 

Histogram là toàn cục vì khi tính giá trị chỉ được tính dựa trên toàn bộ ảnh.
Và được gọi là vector feat gọi là toàn cục.

dựa trên 1 vùng nhất định nào đó thì là cục bộ.

Mạng cnn là cục bộ vì conv bla bla.

Mỗi cái có ưu và nhược riêng.

Hạn chế toàn cục bằng việc chia ra để ra cục bộ.


Màu chủ đạo 

dấu bằng với ngưỡng thì xét như nào. Thì tùy.

Phân biệt zero-shot, few-shot.

Phát biểu bài toán một cách form (hình thức). Sử dụng nền tảng toán học đảm bảo tính đúng đắn về cơ sở lý thuyết.

Có nhiều phương pháp khác nhau nhưng bài toán gốc thường không thay đổi. 

Bài toán ko đổi, thay đổi là cái phương pháp. Phải xác định đúng bài toán. 

Input là tập dữ liệu.
ouput predict phải nằm trong tập dữ liệu. vì nó là close set. 
Còn nếu nằm ngoài là open set. Dữ đoán ảnh ko nằm trong tập huấn luyện.

Còn open set chỉ trả lời unknowned.
zero-shot trả lời đựoc chính xác là cái j lun (?).
one-shot ví dụ 1 ảnh con mèo nhưng nhiều ảnh con chó nhưng vẫn mún predict được. Ko bị bias.
few-shot là cho tập imbalance. là một vài ảnh con mèo.
 
Phải xác định đúng bài toán.

Cho 1 ds n sv. có mssv. có đầy đủ info. 

đặc điểm sup là các đặc điểm độc lập với nhau. áp dụng khi mối quan hệ là độc lập.

### Phát biểu input, output cho chính xác.

Input là nhiều phần tử để tìm ra được phần tử tốt.

Khi đánh giá mô hình. Các image độc lập với nhau cho nên phát biểu bài toán chỉ nói là cần 1 tấm ảnh để đánh giá.
Vì đánh giá các tấm ảnh là riêng biệt. Ta suy về cái đơn giản nhất.

Ở bài toán video, cẩn thận với frame. Xét tính độc lập của frame. 

-> Tóm lại cần xác định đúng bài toán

Giai đoạn huấn luyện (Offline). 
Giai đoạn phân lớp (Online). 
Thông thường trước đây sử dụng parameter của mô hình

Phụ thuộc nhiều vào phân cứng. 
FLOPS đo số phép tính trong quá trình cả học và đánh giá.


Khi lý thuyết thì 
lập confusion matrix. 
tính acc 
- số mẫu dữ đoán đúng nằm trên đường chéo.
mỗi cột là predict, còn mỗi dòng là gt.
tính precision thì tính dựa vào cột dọc của từng label predict.
tính recall thì dựa trên dòng ngang của từng label gt.

### Lưu ý, LT và TH. phải hiểu cách tính và giá trị tính được. 
ví dụ tính ra 10/18 là 10 là cái dự đoán đúng trên 18. 
để nguyên lun chứ ko rút gọn. rút gọn sẽ làm thay đổi ngữ nghĩa.
Khi có sự so sánh giữa 2 mô hình thì phải cần tính ra số. 
Bình thường, lấy 4 chữ số nếu bắt đầu là 0. . Còn bắt đầu khác 0 thì lấy 2 chữ số.
Tuy nhiên tùy đề, người ta cho sẵn bao nhiêu chữ số thập phân r thì nên giữ nguyên.

80% sẽ sai thì bị nhầm. Lưu ý nhé.

đặc trưng về màu sắc. Giới thiệu 4 nhóm dựa trên đặc trưng màu sắc.
về bài toán phân loại là bài toán sup. Sử dụng các độ đo để đánh giá, trong đó nó có acc, precision, recall, confusion matrix.
bài tập Sử dụng knn để huấn luyện mô hình.
Yêu cầu 1 sử dụng vét cạn. 
Yêu cầu 2 đặc trưng nào phụ hợp.
Yêu cầu 3 ảnh nào tốt ảnh nào ko tốt.

Khá quan trọng về ý tưởng.
- deadline 2 tuần.