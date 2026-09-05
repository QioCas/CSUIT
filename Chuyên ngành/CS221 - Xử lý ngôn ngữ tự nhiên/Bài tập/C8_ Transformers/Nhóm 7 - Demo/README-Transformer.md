**Nội dung chính trong Demo**

* Input \& Positional Embeddings: Biểu diễn từ vựng và vị trí của token trong chuỗi.
* Causal Masking: Che giấu thông tin tương lai (Masking out the future) để mô hình học cách dự đoán từ trái sang phải.
* Multi-Head Self-Attention: Cơ chế giúp mô hình chú ý đến các phần ngữ cảnh khác nhau.
* Transformer Block: Tích hợp FeedForward Network, Residual connections và Pre-Layer Normalization.
* Language Modeling Head: Dự đoán xác suất của token tiếp theo.
* Top-k Sampling: Thuật toán lấy mẫu giúp văn bản sinh ra đa dạng và sáng tạo hơn.



**Yêu cầu môi trường:**

Python 3.7+

PyTorch (torch)

Pandas (pandas)

Numpy (numpy)

Jupyter Notebook / Google Colab



**Hướng dẫn chạy Demo**



* Cách 1: Chạy trực tiếp trên Google Colab / Kaggle

  * Mở một Notebook mới trên Google Colab hoặc Kaggle.
  * Bật Runtime GPU (Vào Runtime -> Change runtime type -> Chọn T4 GPU).
  * Upload file Transformer\_Demo.ipynb và mở lên.
  * Tải file dataset netflix\_titles.csv từ Kaggle và upload vào môi trường làm việc (cùng cấp với thư mục chạy code).
  * Chạy tuần tự các ô code (Run All).



* Cách 2: Chạy trên máy cá nhân (Local)

  * Cài đặt các thư viện cần thiết:

code

Bash

pip install torch pandas numpy jupyter



Tải dataset netflix\_titles.csv từ Kaggle và đặt cùng thư mục với file notebook.

Mở terminal tại thư mục đó và khởi động Jupyter:

Mở file .ipynb và chạy từng block code.



**Kết quả**

* Quá trình huấn luyện sẽ mất khoảng 2-5 phút nếu sử dụng GPU.
* Sau khi huấn luyện, mô hình sẽ nhận một câu mồi (Ví dụ: "In a dark city,") và tự động sinh ra một đoạn mô tả phim tiếng Anh khoảng 400 ký tự với cấu trúc và từ vựng học được từ dữ liệu gốc.

