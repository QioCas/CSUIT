Demo Chương 6: Neural Networks (Jurafsky & Martin)

Ứng dụng: Aspect-Based Sentiment Analysis trên tập dữ liệu VLSP 2018

📖 Tổng quan Source Code

Dự án này là bản cài đặt thực hành dựa trên kiến thức của Chương 6: Neural Networks trong giáo trình Speech and Language Processing (Jurafsky & Martin). Dự án không dùng các thư viện NLP xây dựng sẵn (như HuggingFace Transformers) mà tự xây dựng từ đầu (from scratch) các kiến trúc cơ bản bằng PyTorch để bám sát lý thuyết.

Source code (CS221_Chapter6_Demo.ipynb) được chia thành 3 phần chính:

Phần 1: Bài toán XOR (Section 6.2) - Chứng minh sự cần thiết của Lớp ẩn (Hidden Layer) và hàm phi tuyến (ReLU) so với mô hình tuyến tính truyền thống.

Phần 2: FNN & Word Embeddings (Section 6.4 & 6.5) - Áp dụng mạng Feedforward Neural Network kết hợp Ma trận Nhúng (Embeddings) và kỹ thuật Mean-Pooling để xử lý văn bản. Trích xuất và xây dựng Từ điển (Vocabulary) cho cả Từ vựng và Khía cạnh (Aspects).

Phần 3: Huấn luyện, Dự đoán & Tổng hợp (Section 6.6) - Huấn luyện mô hình giải quyết bài toán ABSA (Aspect-Based Sentiment Analysis) trên tập VLSP 2018 (Hotel/Restaurant). Dự đoán cảm xúc từng khía cạnh và sử dụng thuật toán Voting để nội suy ra cảm xúc của toàn bộ câu.

📂 Cấu trúc thư mục (Directory Structure)

Để mã nguồn chạy thành công, bạn cần tổ chức thư mục dự án trên máy tính chính xác như sau (tên file dữ liệu phải giữ nguyên):

CS221_Project/
│
├── CS221_Chapter6_Demo.ipynb                 # File Source Code (Jupyter Notebook)
│
├── 1-VLSP2018-SA-Hotel-train (7-3-2018).txt  # Dữ liệu Train
├── 2-VLSP2018-SA-Hotel-dev (7-3-2018).txt    # Dữ liệu Dev (Validation)
└── 3-VLSP2018-SA-Hotel-test (8-3-2018).txt   # Dữ liệu Test


(Nếu bạn sử dụng bộ dữ liệu Restaurant, hãy đặt 3 file Restaurant tương ứng vào cùng thư mục và đổi tên tham số đọc file trong code).

⚙️ Hướng dẫn Cài đặt (Setup)

Dự án yêu cầu Python 3.7+. Bạn cần mở Terminal (hoặc Command Prompt) và cài đặt các thư viện lõi thông qua pip:

# Cài đặt PyTorch, NumPy, Datasets và Jupyter
pip install torch numpy datasets jupyter


🚀 Hướng dẫn Chạy Source Code (Execution)

Bạn có thể chạy dự án này bằng 1 trong 2 cách: trên máy tính cá nhân (Local) hoặc trên Google Colab.

Cách 1: Chạy trên Google Colab (Khuyên dùng)

Đây là cách nhanh nhất, không lo lỗi môi trường cài đặt.

Truy cập Google Colab.

Chọn File > Upload notebook và tải lên file CS221_Chapter6_Demo.ipynb.

Nhìn sang thanh menu bên trái, bấm vào biểu tượng Thư mục (Files).

Bấm biểu tượng Upload (tải lên) và chọn cả 3 file .txt (Train, Dev, Test) của tập VLSP 2018.
(Lưu ý: Chờ cho vòng tròn upload quay xong 100%).

Trên thanh Menu trên cùng, chọn Runtime > Run all (hoặc bấm Ctrl + F9).

Kéo xuống dưới cùng để xem mô hình in ra kết quả phân tích cho từng câu.

Cách 2: Chạy trên máy cá nhân (Local Machine)

Đảm bảo bạn đã tổ chức cấu trúc thư mục như ở phần Cấu trúc thư mục.

Mở Terminal / Command Prompt, di chuyển (cd) vào thư mục CS221_Project.

Gõ lệnh khởi động Jupyter Notebook:

jupyter notebook


Trình duyệt web sẽ tự động mở ra. Bạn click chọn file CS221_Chapter6_Demo.ipynb.

Trên thanh công cụ của Jupyter, chọn Cell > Run All (hoặc Kernel > Restart & Run All) để thực thi toàn bộ mã nguồn.

📊 Đọc hiểu Kết quả (Expected Output)

Khi quá trình chạy hoàn tất, hãy cuộn xuống các cell cuối cùng của file Notebook. Bạn sẽ thấy Output của mô hình trên tập Test có định dạng tương tự như sau:

[Câu 1]: Tất cả mọi thứ đều sạch sẽ, giường ngủ rất thoải mái. Không có quạt điện mà chỉ có điều hòa nên có chút bất tiện.
Dự đoán từng khía cạnh:
  + HOTEL#CLEANLINESS              ---> POSITIVE
  + ROOM_AMENITIES#COMFORT         ---> NEGATIVE
  + ROOM_AMENITIES#DESIGN&FEATURES ---> NEGATIVE
>>> CẢM XÚC TOÀN CÂU: TIÊU CỰC (NEGATIVE)
---------------------------------------------------------------------------


Giải thích: Mô hình tách được 3 khía cạnh trong câu và nhận diện chính xác sự vắng mặt của quạt điện mang yếu tố "Negative". Sau đó thực hiện Voting (2 Negative > 1 Positive) để gán nhãn toàn bộ câu là Tiêu cực.

Nhóm: 5
Lớp: CS221.Q21.KHTN - Xử lý Ngôn ngữ Tự nhiên