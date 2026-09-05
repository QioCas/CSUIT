# Demo Word Similarity với Word2Vec và t-SNE

Dự án này chứa Jupyter Notebook triển khai mô hình biểu diễn từ **Word2Vec** sử dụng thư viện `gensim` để giải quyết các bài toán về độ tương đồng từ (Word Similarity). Dữ liệu được sử dụng để huấn luyện là tập corpus **text8** (được tải tự động thông qua API của gensim).

Notebook bao gồm các bước thực hiện chính:
1. Tải và đọc dữ liệu văn bản `text8` từ `gensim.downloader`.
2. Khởi tạo và huấn luyện mô hình **Word2Vec** (với kiến trúc Skip-gram hoặc CBOW tùy chỉnh).
3. Thực hiện các truy vấn tìm kiếm từ đồng nghĩa (most similar words) và tính toán độ tương đồng (similarity) giữa các cặp từ.
4. Thực hiện các phép toán trên vector từ (ví dụ: mô hình hóa các mối quan hệ ngữ nghĩa).
5. Đánh giá độ tương đồng từ với dữ liệu con người (Human scores) sử dụng độ đo tương quan **Spearman**.

## 1. Yêu cầu cài đặt (Dependencies)

Các Notebook được viết bằng Python 3 và yêu cầu một số thư viện học máy, xử lý ngôn ngữ tự nhiên thông dụng. Nếu sử dụng môi trường ảo (như Conda, Virtualenv) thì có thể kích hoạt môi trường của mình, sau đó cài đặt trực tiếp qua `pip` hoặc `conda`.

Các thư viện cần thiết:
- `gensim` (Sử dụng lệnh `!pip install gensim` trực tiếp trong notebook)
- `scipy` (để tính toán spearman correlation)
- `pandas` (để đọc dữ liệu đánh giá)

## 2. Hướng dẫn sử dụng
### Chọn cách chạy

#### Cách 1: Chạy bằng Jupyter Notebook (Môi trường Web)
1. Mở terminal và trỏ đến thư mục chứa bài code này.
2. Gõ lệnh:
   ```bash
   jupyter notebook
3. Một giao diện web tại localhost:8888 sẽ mở lên, bạn click chuột trực tiếp để mở file NLP_C5.ipynb.
4. Bấm Run -> Run All Cells trên thanh menu để hệ thống lần lượt tải dữ liệu, huấn luyện mô hình và in ra kết quả đánh giá cuối cùng.

#### Cách 2: Chạy bằng Visual Studio Code (VS Code) / Pycharm
1. Đảm bảo VS Code đã cài đặt extension Jupyter.
2. Mở dự án trong VS Code. Double click để mở file NLP_C5.ipynb.
3. Phía góc phải trên cùng màn hình file mã, Select Kernel và chọn đúng môi trường ảo Python bạn đã thực thi cài đặt thư viện ở bước 1.
4. Bấm nút Run All ở thanh công cụ của Notebook và chờ kết quả in xuất ra ở các cell cuối của file.

#### Cách 3: Đẩy thẳng lên Google Colab
1. Truy cập Google Colab.
2. Chọn tab Upload và tải file NLP_C5.ipynb lên.
3. Chạy cell đầu tiên để cài đặt gensim.
4. Bấm Runtime -> Run all (hoặc Ctrl + F9) để chạy toàn bộ file trên môi trường máy chủ của Google.