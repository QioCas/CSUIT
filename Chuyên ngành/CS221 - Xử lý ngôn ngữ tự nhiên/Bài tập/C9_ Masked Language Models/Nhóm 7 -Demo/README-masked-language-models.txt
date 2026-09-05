
# Nội dung Demo

Demo bao gồm 2 phần chính:

1. **Phần 1 - Contextual Embeddings:** 
   - Chứng minh sự khác biệt giữa Static Embeddings (như Word2Vec) và Contextual Embeddings (BERT).
   - Sử dụng Cosine Similarity để cho thấy BERT tạo ra các vector khác nhau cho cùng một từ đa nghĩa (từ "mouse") tùy thuộc vào ngữ cảnh (con chuột động vật vs. chuột máy tính).

2. **Phần 2 - Fine-Tuning for Sequence Classification (Mục 9.4.1):**
   - Hướng dẫn cách tinh chỉnh (fine-tune) mô hình pre-trained BERT cho bài toán phân loại văn bản (Text Classification).
   - **Dataset:** Sử dụng tập dữ liệu **IMDB Movie Reviews** (được tải trực tiếp qua thư viện Hugging Face Datasets) để dự đoán cảm xúc (Tích cực/Tiêu cực) của một đoạn đánh giá phim.

# Yêu cầu hệ thống & Cài đặt

Bản demo sử dụng thư viện PyTorch và hệ sinh thái của Hugging Face. Để chạy code, cần cài đặt các thư viện sau:

```bash
pip install transformers datasets evaluate torch scikit-learn


# Hướng dẫn chạy Demo

Mở file .ipynb bằng Jupyter Notebook, Jupyter Lab, hoặc upload lên Google Colab.
Chạy lần lượt từng ô lệnh (Cell) từ trên xuống dưới.
Ở Phần 2, mô hình sẽ bắt đầu quá trình huấn luyện (Fine-tuning) qua 3 epochs. Xem kết quả đánh giá (Accuracy) sau khi train xong.
Ở cell cuối cùng, có thể tự thay đổi nội dung biến test_reviews để thử nghiệm khả năng dự đoán của mô hình với những câu văn riêng.

# Lưu ý 

Nên sử dụng GPU: Quá trình Fine-tuning mô hình BERT yêu cầu tài nguyên tính toán lớn. Khuyến khích chạy file trên Google Colab và bật chế độ GPU (Runtime -> Change runtime type -> Chọn T4 GPU) để tiết kiệm thời gian.
