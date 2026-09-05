# Aspect-Based Sentiment Analysis với Mạng Nơ-ron (FFNN) và FastText

Dự án này chứa Jupyter Notebook (`NLP_C6.ipynb`) triển khai mô hình học sâu **Feed-Forward Neural Network (FFNN)** kết hợp cùng biểu diễn từ **FastText** phục vụ cho bài toán Khai phá ý kiến (Aspect-Based Sentiment Analysis). Dữ liệu được sử dụng là tập **đánh giá nhà hàng (Restaurant)** của cuộc thi **VLSP 2018**.

Bài toán được tiếp cận dưới dạng **Phân loại đa nhãn (Multi-label Classification)**, nơi mỗi câu bình luận có thể chứa nhiều khía cạnh (Aspect) và cảm xúc (Polarity) khác nhau.

Notebook bao gồm các bước thực hiện chính:
1. Đọc và tiền xử lý làm sạch dữ liệu văn bản từ cuộc thi VLSP 2018.
2. Trích xuất và chuẩn hóa danh sách các nhãn (ví dụ: chuyển đổi từ `{FOOD#QUALITY, positive}` sang dạng chuỗi hợp nhất).
3. Chuyển đổi nhãn về dạng One-Hot đa nhãn sử dụng `MultiLabelBinarizer`.
4. Tải và ứng dụng bộ pre-trained Word Embedding **FastText** Tiếng Việt (`cc.vi.300.vec`).
5. Biểu diễn câu (Sentence Representation) bằng kỹ thuật tính trung bình các vector từ (Mean Pooling).
6. Xây dựng và huấn luyện mô hình học sâu với **TensorFlow/Keras**.
7. Dự đoán thử nghiệm và lưu mô hình ra định dạng `.keras`.

## 1. Yêu cầu cài đặt (Dependencies)

Các Notebook được viết bằng Python 3. Bạn nên sử dụng môi trường ảo (Conda, Virtualenv) và cài đặt các thư viện thông qua `pip`.

Các thư viện cần thiết:
- `numpy`, `pandas`
- `scikit-learn`
- `tensorflow`
- `gensim` (Sử dụng lệnh `!pip install gensim` trực tiếp trong notebook)
- `re`

*Lưu ý: Quá trình chạy sẽ tự động tải file embedding FastText (nặng khoảng ~1.1GB).*

## 2. Hướng dẫn sử dụng
### Chọn cách chạy

#### Cách 1: Chạy bằng Jupyter Notebook (Môi trường Web)
1. Mở terminal và trỏ đến thư mục chứa bài code này.
2. Gõ lệnh:
   ```bash
   jupyter notebook
3. Một giao diện web tại localhost:8888 sẽ mở lên, bạn click chuột trực tiếp để mở file NLP_C6.ipynb.
4. Bấm Run -> Run All Cells trên thanh menu để hệ thống lần lượt tải dữ liệu, huấn luyện mô hình và in ra kết quả đánh giá cuối cùng.

#### Cách 2: Chạy bằng Visual Studio Code (VS Code) / Pycharm
1. Đảm bảo VS Code đã cài đặt extension Jupyter.
2. Mở dự án trong VS Code. Double click để mở file NLP_C5.ipynb.
3. Phía góc phải trên cùng màn hình file mã, Select Kernel và chọn đúng môi trường ảo Python bạn đã thực thi cài đặt thư viện ở bước 1.
4. Bấm nút Run All ở thanh công cụ của Notebook và chờ kết quả in xuất ra ở các cell cuối của file.

#### Cách 3: Đẩy thẳng lên Google Colab
1. Truy cập Google Colab.
2. Chọn tab Upload và tải file NLP_C6.ipynb lên.
3. Tải các file dữ liệu .txt của VLSP 2018 lên môi trường session của Colab (hoặc upload qua cell thứ nhất trong code).
4. Bấm Runtime -> Run all (hoặc Ctrl + F9) để tận dụng băng thông và GPU của Google để tải FastText cũng như huấn luyện mô hình nhanh hơn.