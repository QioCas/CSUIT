# Word2Vec: Arxiv Paper Abstracts Embedding

Dự án này triển khai mô hình học máy Word2Vec để trích xuất biểu diễn vector (word embeddings) từ kho tóm tắt các bài báo khoa học trên Arxiv.

## 1. Thư viện sử dụng
Các thư viện và module được sử dụng để xây dựng mô hình:
* **[Gensim](https://radimrehurek.com/gensim/)**: Thư viện lõi xử lý ngôn ngữ tự nhiên, cung cấp thuật toán `Word2Vec` và công cụ tiền xử lý văn bản `simple_preprocess`.
* **[Underthesea](https://github.com/undertheseanlp/underthesea)**: Cài đặt kèm theo môi trường hỗ trợ xử lý NLP tiếng Việt (trong ngữ cảnh code hiện tại, dữ liệu tập trung vào tiếng Anh).
* **[Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)**: Thư viện chuẩn của Python, dùng để lấy số lượng core CPU (`cpu_count`) nhằm tối ưu hóa tiến trình huấn luyện đa luồng.
* **[CSV](https://docs.python.org/3/library/csv.html) & [Sys](https://docs.python.org/3/library/sys.html)**: Hỗ trợ đọc file tập dữ liệu cấu trúc cực lớn với cấu hình cấp phát giới hạn bộ nhớ `csv.field_size_limit(sys.maxsize)`.

---

## 2. Định dạng dữ liệu (Format Data)
* **Training Data:** * Nguồn: Các file CSV (`arxiv_data.csv`, `arxiv_data_210930-054931.csv`).
  * Định dạng xử lý: Đọc và trích xuất chuỗi văn bản từ cột `abstracts`. Mỗi tóm tắt được đưa qua pipeline `simple_preprocess(deacc=True)` để chuẩn hóa thành list các token (từ đơn) viết thường, loại bỏ toàn bộ dấu câu và ký tự đặc biệt.
* **Test Data:** * Định dạng: Danh sách các từ khóa chuyên ngành mục tiêu dưới dạng mảng chuỗi `['convolutional', 'quantum', 'transformer', 'topology']`.
* **Command Line:** * Cài đặt dependencies: `pip install gensim underthesea`.
  * Thực thi tiêu chuẩn: Khởi chạy luồng chính thông qua block `if __name__ == "__main__": main()`.

---

## 3. Quá trình xây dựng mô hình
Quá trình huấn luyện được thiết kế theo kiến trúc Skip-gram, bao gồm 4 bước:

1. **Khởi tạo Corpus (Streaming Iterator):** Sử dụng Class `ArxivCSVCorpus` làm một generator (`yield`).
2. **Cấu hình siêu tham số (Hyperparameters):**
   * `vector_size=200`: Xây dựng không gian vector biểu diễn từ có 200 chiều.
   * `window=5`: Khoảng cách cửa sổ ngữ cảnh là 5 từ xung quanh.
   * `min_count=10`: Bỏ qua các từ xuất hiện dưới 10 lần trong toàn bộ corpus.
   * `sg=1`: Dùng thuật toán **Skip-gram** (dùng từ hiện tại để dự đoán ngữ cảnh), cho hiệu suất trích xuất đặc trưng tốt hơn đối với các từ hiếm trong tập dữ liệu khoa học.
3. **Huấn luyện mô hình:**
   Mô hình lặp qua dữ liệu `epochs=5` lần. Tiến trình được tăng tốc tối đa nhờ tham số `workers` gán bằng tổng số luồng thực lý của CPU.
4. **Lưu trữ (Persistence):**
   Trọng số mô hình sau hội tụ được lưu xuống file nhị phân `arxiv_word2vec.model` để tái sử dụng.

---

## 4. Demo
Để kiểm chứng hoạt động của mô hình, chạy file mã nguồn trực tiếp qua Terminal:
```bash
python <tên_file>.py