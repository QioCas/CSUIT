# CHƯƠNG 5: WORD EMBEDDING VỚI WORD2VEC (SGNS)

Dự án này thực hiện hóa **giả thuyết phân phối (distributional hypothesis)** trong xử lý ngôn ngữ tự nhiên (NLP), chứng minh rằng ý nghĩa của một từ có thể được định nghĩa thông qua các từ hàng xóm hoặc môi trường ngữ pháp xung quanh nó. Dự án được thực hiện bởi **Nhóm 5**.

---

## 📌 Tổng Quan Dự Án

* **Mục đích:** Huấn luyện mô hình nhúng từ (Word Embedding) để học các dense vectors (vector dày đặc) mang ngữ nghĩa cao từ văn bản thô, thay thế cho các biểu diễn vector thưa thớt truyền thống.
* **Bộ dữ liệu (Dataset):** Sử dụng `Text8` - một tập dữ liệu sạch gồm 17 triệu từ được trích xuất từ Wikipedia. Đây là dataset chuẩn lý tưởng cho việc học biểu diễn (Representation Learning) nhờ tính đa dạng và phong phú về mặt từ vựng.
* **Thuật toán:** Kiến trúc **Skip-gram kết hợp Negative Sampling (SGNS)** thuộc mô hình Word2Vec.

---

## 🛠️ Cấu Hình Mô Hình (Hyperparameters)

Mô hình được cấu hình mạnh mẽ với các tham số tối ưu để bắt được quan hệ ngữ nghĩa rộng:
* `vector_size = 300`: Không gian biểu diễn 300 chiều.
* `window = 7`: Cửa sổ ngữ cảnh mở rộng (7 từ trước và 7 từ sau).
* `min_count = 5`: Loại bỏ các từ hiếm xuất hiện ít hơn 5 lần.
* `sg = 1`: Kích hoạt kiến trúc Skip-gram.
* `negative = 15`: Tăng số lượng mẫu âm (negative samples) để nâng cao khả năng phân biệt ngữ nghĩa.
* `epochs = 10`: Huấn luyện qua 10 lượt dữ liệu.

---

## 📊 Kết Quả Phân Tích Dữ Liệu (EDA)

Trước khi huấn luyện, dữ liệu được thống kê và đạt được các chỉ số sau:
* **Tổng số đoạn văn bản:** 1,701 đoạn.
* **Độ dài trung bình mỗi đoạn:** ~9,997 từ.
* **Tổng số lượng từ trong Corpus:** 17,005,207 từ.
* **Kích thước từ vựng (Vocabulary size):** 253,854 từ duy nhất.
* **Top 5 từ xuất hiện nhiều nhất:** `the` (1.06M), `of` (593K), `and` (416K), `one` (411K), `in` (372K). *(Tần suất unigram này liên quan trực tiếp đến trọng số $\alpha = 0.75$ trong kỹ thuật Negative Sampling).*

---

## 🚀 Tiến Trình Huấn Luyện (Training Loss)

Mô hình sử dụng `MonitorCallback` để theo dõi giá trị hàm mất mát qua từng Epoch. Thống kê cho thấy Loss tăng tích lũy và đạt trạng thái bão hòa ở những epoch cuối:
* **Epoch 1:** Loss = 52,594,644.00
* **Epoch 5:** Loss = 104,033,488.00
* **Epoch 9 & 10:** Loss = 134,217,728.00 (Đã đạt mức hội tụ và bão hòa).

---

## 🎯 Đánh Giá Đặc Tính Ngữ Nghĩa

### 1. Kiểm tra sự tương đồng (Word Similarity)
Thử nghiệm tìm kiếm các từ gần nhất với từ mẫu `"cherry"` bằng độ tương đồng Cosine:
* `cherries`: 0.5358 (Quan hệ hình thái số ít - số nhiều)
* `raisin`: 0.5277 (Quan hệ cùng nhóm/trường ngữ nghĩa thực phẩm)
* `dogwood`: 0.5275
* `cucumber`: 0.5221

> **Nhận xét:** Trong không gian 300 chiều, các vector loãng hơn nên độ tương đồng Cosine ở mức vừa phải, tuy nhiên độ chính xác về mặt "hàng xóm" (neighbors) trong trường ngữ nghĩa là cực kỳ chính xác.

### 2. Khả năng loại suy (Analogy)
Thực hiện phép toán kiểm tra mô hình hình bình hành (parallelogram model):
$$\vec{\text{King}} - \vec{\text{Man}} + \vec{\text{Woman}} \approx \vec{\text{Queen}}$$

* **Kết quả thực tế:** Mô hình trả về chính xác từ `queen`. Điều này chứng minh mô hình đã nắm bắt thành công các thuộc tính quan hệ (relational properties) tinh tế giữa các thực thể giới tính và vương quyền.

---

## 📉 Trực Quan Hóa Với t-SNE

Dự án sử dụng thuật toán **t-SNE** (với `perplexity=3`, `random_state=42`) để giảm chiều dữ liệu từ không gian 300 chiều về không gian 2 chiều nhằm mục đích trực quan hóa mối liên kết giữa 9 từ mẫu: `['cherry', 'strawberry', 'apple', 'digital', 'computer', 'information', 'data', 'university', 'student']`.

![t-SNE Visualization](https://via.placeholder.com/600x480.png?text=t-SNE+Word+Embeddings+Plot) *(Hình ảnh đồ thị scatter plot sinh ra từ thư viện Matplotlib trong code)*

> **Nhận xét đồ thị:**
> * Mô hình phân cụm rất tốt theo ngữ nghĩa thực tế (distributional semantics). Các từ phân rõ theo từng nhóm riêng biệt như nhóm Công nghệ (`digital`, `computer`, `data`, `information`) và nhóm Giáo dục (`university`, `student`).
> * Đặc biệt, từ **`apple`** nằm ở khoảng giữa ranh giới của nhóm trái cây và nhóm công nghệ. Điều này phản ánh chính xác ngữ cảnh thực tế của từ này (vừa là quả táo, vừa là tập đoàn công nghệ lớn).

---
## 💻 Hướng Dẫn Chạy Trên Google Colab

Mặc dù thuật toán `Word2Vec` của thư viện `Gensim` sử dụng CPU làm phần cứng tính toán chính, việc chuyển đổi sang Runtime **GPU T4** trên Colab vẫn được khuyến nghị để hệ thống cấp phát cấu hình RAM nền mạnh mẽ hơn, tránh bị tràn bộ nhớ khi xử lý dữ liệu lớn.

1. **Mở file:** Tải file `C5_NLP.ipynb` lên [Google Colab](https://colab.research.google.com/) hoặc mở trực tiếp từ Google Drive của bạn.
2. **Cấu hình môi trường (Khuyến nghị):**
   * Trên thanh menu, chọn **Runtime** *(Thời gian chạy)* -> **Change runtime type** *(Thay đổi loại thời gian chạy)*.
   * Tại mục **Hardware accelerator** *(Bộ tăng tốc phần cứng)*, chọn **T4 GPU** (hoặc để mặc định **CPU** nếu tài nguyên GPU của bạn bị giới hạn, mô hình vẫn chạy bình thường trên CPU).
   * Nhấn **Save** *(Lưu)*.
3. **Thực thi:** Vào lại **Runtime** -> Chọn **Run all** *(Chạy tất cả)* hoặc nhấn `Ctrl + F9` / `Cmd + F9`.

---

## 💻 Yêu Cầu Phần Cứng Khi Chạy Môi Trường Local (Máy Cá Nhân)

Nếu chạy file Notebook này trực tiếp trên máy tính cá nhân thay vì Google Colab, bạn cần lưu ý cấu hình sau:

* **Card đồ họa (GPU):** **Không yêu cầu** (Do thư viện `Gensim` không hỗ trợ huấn luyện Word2Vec trên GPU).
* **Bộ nhớ RAM (Quan trọng nhất):** Tối thiểu **12GB RAM** (Khuyến nghị **16GB RAM** trở lên). Do toàn bộ dữ liệu thô và ma trận biểu diễn 300 chiều của $253,854$ từ vựng duy nhất sẽ được nạp và xử lý hoàn toàn trên RAM.
* **Bộ vi xử lý (CPU):** Khuyến nghị CPU từ **4 nhân / 8 luồng** trở lên. Mô hình đã được cấu hình tham số `workers=4` để tận dụng tính năng đa luồng (Multi-threading) giúp đẩy nhanh tốc độ hội tụ qua 10 Epoch.
* **Ổ cứng:** Trống tối thiểu **500MB** (Khuyến nghị ổ SSD) để tải, giải nén dữ liệu `text8` và lưu file model sau khi huấn luyện xong.

