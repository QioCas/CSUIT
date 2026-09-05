**Demo Xử lý Ngôn ngữ Tự nhiên: Neural Network (Chương 6)**



1. Nội dung Demo:
* Tiền xử lý văn bản: Làm sạch văn bản, tách từ (tokenization) và xây dựng bộ từ vựng (Vocabulary).
* Word Embeddings \& Mean-Pooling (Mục 6.5): Biểu diễn từ thành vector liên tục và dùng phép lấy trung bình (mean-pooling) để đại diện cho toàn bộ câu.
* Mạng nơ-ron truyền thẳng (Mục 6.3): Xây dựng mô hình (MLP) với các lớp ẩn và hàm kích hoạt ReLU sử dụng PyTorch.
* Huấn luyện mô hình (Mục 6.6): Áp dụng hàm mất mát Cross-Entropy và thuật toán Lan truyền ngược (Backpropagation) để tối ưu hóa trọng số.
* Dự đoán thực tế (Inference): Dùng mô hình đã huấn luyện để phân tích cảm xúc các câu tiếng Anh bất kỳ.



2\. Tập dữ liệu (Dataset)

* Demo sử dụng bộ dữ liệu thực tế IMDB Movie Reviews (50.000 đánh giá phim tích cực/tiêu cực).

Nguồn:Kaggle - IMDB Dataset of 50K Movie Reviews



3\. Yêu cầu môi trường

* Python 3.7+
* Môi trường: Jupyter Notebook hoặc Google Colab.
* Cài đặt các thư viện cần thiết bằng lệnh sau:

code

Bash

pip install torch pandas numpy scikit-learn tqdm



4\. Cách chạy Demo

* Cách 1: Chạy trên máy tính cá nhân (Local)

Cài đặt các thư viện yêu cầu như trên.

Đảm bảo file IMDB Dataset.csv nằm cùng thư mục với file notebook (.ipynb).

Mở terminal/command prompt, gõ jupyter notebook và mở file demo.

Chọn Kernel -> Restart \& Run All để chạy toàn bộ các khối code từ trên xuống dưới.



* Cách 2: Chạy trên Google Colab

Tải file .ipynb lên Google Colab.

Tải file IMDB Dataset.csv lên phần Files của Colab.

Chọn Runtime -> Run all để thực thi toàn bộ code.

