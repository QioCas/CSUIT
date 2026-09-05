# Aspect-Based Sentiment Analysis - Restaurant Reviews

### 1. Data Parsing
Dữ liệu thô ban đầu có dạng văn bản lồng ghép nhãn cảm xúc: `{ENTITY#ATTRIBUTE, polarity}`. 
* **Ý tưởng:** Để tương thích với mô hình Softmax, bài toán được chuyển đổi (Flatten) thành dạng ma trận nhãn. 
* Hệ thống trích xuất 12 cặp khía cạnh (Aspects) tiêu biểu (như `FOOD#QUALITY`, `SERVICE#GENERAL`, `RESTAURANT#PRICES`) thành 12 cột biến mục tiêu độc lập.
* Mỗi khía cạnh được gán một trong 4 giá trị số học:
  * `0`: Null
  * `1`: Positive
  * `2`: Negative
  * `3`: Neutral

### 2. Text Preprocessing
Các đánh giá thực tế thường chứa rất nhiều nhiễu. Pipeline tiền xử lý bao gồm các bước:
* **Xử lý Emoji:** Sử dụng thư viện `emoji` để loại bỏ các biểu tượng cảm xúc và thay thế bằng khoảng trắng, tránh hiện tượng dính chữ (vd: "ngon👍quá" -> "ngon quá").
* **Chuẩn hóa cơ bản:** Chuyển toàn bộ văn bản về chữ thường (lowercase), loại bỏ dấu câu (punctuation) và chuẩn hóa khoảng trắng.
* **Tách từ tiếng Việt (Word Segmentation):** Tích hợp thư viện `underthesea` để gom các âm tiết thành từ ghép có nghĩa (vd: "không gian" -> "không_gian", "phục vụ" -> "phục_vụ"). Điều này giúp mô hình hiểu đúng ngữ cảnh và giảm nhiễu cho bước sau.

### 3. Feature Extraction
* Chuyển đổi ngôn ngữ tự nhiên thành vector số học bằng **TF-IDF Vectorizer**.
* Sử dụng N-grams với `ngram_range=(1, 2)` nhằm bắt được các cụm từ đa âm mang sắc thái cảm xúc (ví dụ: "giá_rẻ", "không_ngon").

### 4. Modeling & Evaluating
* **Huấn luyện:** Áp dụng `MultiOutputClassifier` để bọc mô hình `LogisticRegression` (với `multi_class='multinomial'` và `class_weight='balanced'`), cho phép huấn luyện song song 12 mô hình Softmax cho 12 khía cạnh.
* **Evaluating:** Kết quả dự đoán được xuất nhanh dưới dạng **Confusion Matrix** (Ma trận nhầm lẫn). Hệ thống tự động vẽ một lưới đồ thị 4x3 trực quan hiển thị hiệu suất phân loại của cả 4 lớp cho toàn bộ 12 khía cạnh, giúp nhanh chóng nhận diện điểm yếu của mô hình.
* **Xuất dữ liệu:** Toàn bộ metrics (Precision, Recall, F1-score) của mỗi aspect được lưu tự động ra file `.json`


## Thư viện sử dụng
* `pandas`, `numpy`: Xử lý ma trận và bảng dữ liệu.
* `scikit-learn`: Xây dựng pipeline TF-IDF và mô hình Machine Learning.
* `underthesea`: Tách từ (Word Segmentation) chuyên dụng cho tiếng Việt.
* `emoji`: Tiền xử lý biểu tượng cảm xúc.
* `matplotlib`, `seaborn`: Trực quan hóa dữ liệu (Confusion Matrix).