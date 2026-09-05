# Demo NLP: Phân loại Cảm xúc với RNN và LSTM

Notebook sử dụng tập dữ liệu **IMDB Movie Reviews** (có sẵn qua Keras) để giải quyết bài toán Phân loại chuỗi (Sequence Classification): Dự đoán một bình luận phim là **Tích cực (Positive)** hay **Tiêu cực (Negative)**.

## Nội dung trong Demo

File Jupyter Notebook (`.ipynb`) được chia thành các phần chính sau:

1. **Khám phá và Tiền xử lý dữ liệu:** Tải tập dữ liệu IMDB, chuyển đổi văn bản thành các chuỗi số (Word Indices) và áp dụng kỹ thuật Padding để đồng bộ độ dài các câu.
2. **Simple RNN:** Xây dựng mạng nơ-ron hồi quy cơ bản (Elman Network) kết hợp với Word Embedding.
3. **LSTM (Long Short-Term Memory):** Nâng cấp kiến trúc với LSTM để khắc phục vấn đề tiêu biến đạo hàm (Vanishing Gradients) khi xử lý các câu dài.
4. **Bidirectional LSTM:** Xây dựng mô hình LSTM 2 chiều (trái sang phải và phải sang trái) giúp nắm bắt bối cảnh văn bản tốt hơn.
5. **Đánh giá & So sánh:** Trực quan hóa độ chính xác (Accuracy) của 3 mô hình trên tập Validation.
6. **Inference (Dự đoán thực tế):** Viết hàm tự động dự đoán cảm xúc cho một câu bình luận tiếng Anh bất kỳ do người dùng nhập vào.

## Yêu cầu hệ thống (Dependencies)

Để chạy được file demo này, cần cài đặt các thư viện Python sau:
- `tensorflow` (bao gồm Keras)
- `numpy`
- `matplotlib`

## Cách chạy Demo

1. Truy cập [Google Colab](https://colab.research.google.com/).
2. Chọn **File > Upload notebook** và tải lên file `.ipynb`.
3. Vào **Runtime > Change runtime type**, chọn **GPU** để huấn luyện mô hình nhanh hơn (không bắt buộc).
4. Nhấn **Run All** (hoặc `Ctrl + F9`) để chạy toàn bộ các ô code từ trên xuống dưới.