# NLP Demo: Phân loại văn bản bằng Mạng Nơ-ron (PyTorch)

## 1. Giới thiệu
Dự án này là một bài thực hành (demo) cơ bản về Xử lý Ngôn ngữ Tự nhiên (NLP) sử dụng Mạng Nơ-ron tiến thẳng (**Feed-Forward Neural Network - FNN**). Mô hình được xây dựng bằng framework **PyTorch**, kết hợp với **Scikit-learn** để chuyển đổi dữ liệu dạng văn bản thành các vector đặc trưng (**TF-IDF**).

Mục tiêu của dự án là huấn luyện một mô hình AI có khả năng đọc một câu văn tiếng Anh và dự đoán xem câu văn đó thuộc chủ đề nào (ví dụ: vũ trụ, xe cộ, đồ họa máy tính, hay y tế).

---

## 2. Dataset (20 Newsgroups)
Dự án sử dụng bộ dữ liệu kinh điển **20 Newsgroups** được tích hợp sẵn trong thư viện scikit-learn. Đây là tập hợp các bài đăng trên các diễn đàn tin tức (newsgroup) phân theo nhiều chủ đề khác nhau.

Để quá trình demo và huấn luyện diễn ra nhanh chóng, notebook này chỉ trích xuất và sử dụng **4 chủ đề (categories)** chính:
* **sci.space** (Khoa học - Vũ trụ)
* **rec.autos** (Giải trí - Xe cộ)
* **comp.graphics** (Máy tính - Đồ họa)
* **sci.med** (Khoa học - Y tế)

**Kỹ thuật xử lý dữ liệu:**
* Sử dụng `TfidfVectorizer` (với `max_features=3000` và loại bỏ `stop_words='english'`) để chuyển đổi văn bản raw thành các vector số thực (Input Vector X).

---

## 3. Cách tự chạy lại (How to Run)
Bạn có thể chạy lại mã nguồn này theo hai cách phổ biến:

### Cách 1: Chạy trên Google Colab (Khuyên dùng)
Vì notebook đã được thiết lập sẵn trên Colab (có metadata sử dụng T4 GPU), đây là cách nhanh nhất và không cần cài đặt môi trường:
1. Tải file `NLP_Demo_NN.ipynb` về máy tính.
2. Truy cập **Google Colab**.
3. Chọn **File -> Upload notebook** và tải file lên.
4. (Tùy chọn) Vào **Runtime -> Change runtime type** -> Chọn **T4 GPU** để tăng tốc độ huấn luyện.
5. Nhấn **Runtime -> Run all** (hoặc `Ctrl + F9`) để chạy toàn bộ code.

### Cách 2: Chạy Local trên máy tính cá nhân
Nếu bạn muốn chạy trên máy tính cá nhân, bạn cần cài đặt Python và các thư viện cần thiết.
1. Cài đặt Python (khuyên dùng phiên bản >= 3.8).
2. Cài đặt các thư viện thông qua terminal/command prompt:
```bash
pip install torch pandas scikit-learn jupyter
```
3. Mở Jupyter Notebook trong thư mục chứa file:
```bash
jupyter notebook
```
4. Mở file NLP_Demo_NN.ipynb và tiến hành chạy từng cell (ô code).

---
## 4. Nội dung thực hành
Notebook được chia thành 4 phần chính, mô phỏng một pipeline học máy (Machine Learning Pipeline) hoàn chỉnh:

Phần 1 - Thư viện: Import các công cụ cần thiết như torch, pandas, sklearn.feature_extraction.text (TF-IDF), v.v.

Phần 2 - Data: * Tải bộ dữ liệu 20newsgroups (tập train).

Fit và transform văn bản thành ma trận TF-IDF 3000 chiều.

Phần 3 - Model: * Xây dựng kiến trúc Mạng nơ-ron (class model) kế thừa từ nn.Module.

Cấu trúc mạng gồm: Input Layer (3000) -> Hidden Layer (128, ReLU) -> Output Layer (4 classes, Softmax lúc suy luận).

Phần 4 - Train & Test:

Chuyển đổi dữ liệu sang TensorDataset và DataLoader để train theo batch (batch_size=64).

Huấn luyện mô hình trong 20 Epochs với Optimizer Adam và Loss function CrossEntropyLoss. Mô hình đạt độ chính xác hội tụ tuyệt đối trên tập train.

Đánh giá mô hình trên tập Test độc lập, đạt độ chính xác cao (~93.14%).

Inference (Suy luận): Viết hàm predict_topic để đưa các câu văn mới toanh vào (như "NASA launched a new rocket to the moon.") và in ra kết quả dự đoán cùng độ tự tin (Confidence Score). Kết quả demo cho thấy mô hình nhận diện chính xác 100% các câu ví dụ.