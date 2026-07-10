# Đề bài

## Assignment 0 - Tìm hiểu Decision Tree - Deadline: ngày 28/09/2025

Chào cả lớp,

Trong bài tập cá nhân này chúng ta cần viết một báo cáo về:

1/ Decision Trees trong sklearn. Công dụng & cách sử dụng.

2/ Ít nhất 01 thuật toán xây dựng Decision Tree. Và các tiêu chuẩn split: gini, entropy,...

Yêu cầu:

Nộp 01 file pdf báo cáo (khuyến khích dùng LaTeX để soạn thảo), đặt tên dạng BT0_MSSV.pdf với MSSV là mã số sinh viên của mỗi bạn. (Khuyến khích sử dụng overleaf https://www.overleaf.com/project)
Viết báo cáo bằng tiếng Việt, trình bày gọn gàng, sạch sẽ, chuyên nghiệp (không dài quá 10 trang A4).
Trong báo cáo có link tới Google Colab chứa source code của demo (để chế độ public).
Tài liệu tham khảo:

https://scikit-learn.org/stable/modules/tree.html

---

## Assignment 1 - Exploratory Data Analysis - Deadline: ngày 21/09/2025

Chào cả lớp,

Trong bài tập này, các em cần:

Áp dụng những hàm plot có sẵn trong file hướng dẫn và tìm hiểu thêm các cách plot khác để khảo sát và phân tích bộ dữ liệu "penguins". 
Tìm hiểu cách chia dataset thành tập train và tập test (hint: Hàm train_test_split của sklearn). Tập train dùng để huấn luyện mô hình Decision Tree, và tập test để kiểm thử độ chính xác của mô hình Decision Tree (hint: hàm accuracy_score của sklearn).
Các em hãy thử một số setting khác nhau cho hyperparameter max_depth và cho biết nhận xét của em về hyperparameter này ảnh hưởng thế nào tới độ chính xác của mô hình trên tập test. (Viết nhận xét ở dạng comment trực tiếp trong file ipynb). 
Lưu ý: 
Khi sử dụng hàm train_test_split và khi khởi tạo Decision Tree cần đặt random_state là mã số sinh viên của mỗi bạn.
Bộ dữ liệu penguins có các mẫu dữ liệu bị thiếu hụt thông tin (missing data). Các em cần tìm hiểu cách xử lý sao cho phù hợp và viết lại nhận xét mình đã xử lý missing data như thế nào. (Viết nhận xét ở dạng comment trực tiếp trong file ipynb). 
Deadline: 23:59 ngày 21/09/2025. Nộp bài sau ngày 21/09/2025 sẽ bị trừ điểm dần. Sau ngày 28/09/2025 sẽ không nhận thêm bài nộp.

File nộp: 1 file BT1_MSSV.ipynb với MSSV là mã số sinh viên của mình.

---


## Assignment 2 - Bias-Variance Trade-off - Deadline: 10/11/2025


Các yêu cầu hoàn thành
Opened: Chủ Nhật, 26 tháng 10 2025, 12:00 AM
Due: Thứ Hai, 10 tháng 11 2025, 11:59 PM
Trong bài tập này, chúng ta sẽ lập trình và trực quan hóa kết quả thực nghiệm để mô phỏng ví dụ trong trang 60-70 của slides đính kèm.

Bài làm trong 1 file ipynb đặt tên BT2_MSSV.ipynb (với MSSV là mã số sinh viên của mỗi bạn) cần thể hiện kết quả chạy của các thực nghiệm sau đây:

Experiment 1:

Tạo 03 bộ dữ liệu D1, D2, D3. Mỗi bộ dữ liệu gồm có 1 tập train gồm N=10 điểm dữ liệu và 1 tập test gồm N=10 điểm dữ liệu. Các điểm dữ liệu (x,y) có giá trị input x được phát sinh ngẫu nhiên trong khoảng (0,1) và giá trị target y = f(x)=sin(1 + x^2) + ε với ε tuân theo phân phối chuẩn N(0,σ=0.03) như trong trang 60-61 của slides (standard deviation là 0.03).
Với mỗi bộ dữ liệu D1, D2, D3, sử dụng tập train để huấn luyện 9 mô hình polynomial regression có bậc (degree) từ 1-9 như trong trang 70 của slides. Các em cần plot được minh họa ghép 9 đồ thị vào trong 1 hình như trong trang 70 này.
Với bộ dữ liệu D1, tính giá trị E_in (sử dụng tập train) và E_out (sử dụng tập test) tương ứng cho 9 mô hình và tạo ra 1 bảng thống kê kết quả như trang 68 của slides. Trong file ipynb cần thể hiện bảng thống kê kết quả này.
Experiment 2: Làm tương tự như Experiment 1 với N = 100 điểm dữ liệu.

Experiment 3: Làm tương tự như Experiment 1 với N = 1000 điểm dữ liệu.

Ở cuối file nộp ipynb, cần viết nhận xét trả lời các câu hỏi sau:

Tăng độ phức tạp của mô hình ảnh hưởng thế nào đến bias?
Tăng độ phức tạp của mô hình ảnh hưởng thế nào đến variance?
Tăng kích thước tập train ảnh hưởng thế nào đến bias?
Tăng kích thước tập train ảnh hưởng thế nào đến variance?
Lưu ý: Bắt buộc phải sử dụng các hàm phát sinh số ngẫu nhiên của numpy.random (ví dụ: np.random.rand, np.random.random, np.random.randn, ...).

Ở đầu file ipynb cần có đoạn code sau đây với MSSV là mã số sinh viên của mỗi bạn.

import numpy as np
np.random.seed(MSSV)

Deadline: 10/11/2025. Nộp bài sau ngày 10/11/2025 sẽ bị trừ điểm dần dần. Sau ngày 17/11/2025 sẽ không nhận thêm bài nộp nữa. 


