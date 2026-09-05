# Demo: Dependency Parsing (Chương 19)

## Hướng dẫn chạy Demo

1. Mở file `.ipynb`.
2. Chạy **Cell 1** để hệ thống tự động cài đặt các thư viện cần thiết (`spacy`, `conllu`, `networkx`, `matplotlib`) và tải mô hình tiếng Anh (`en_core_web_sm`).
3. Chạy **Cell 2** để tự động tải tập dữ liệu thật (dataset) trực tiếp từ kho lưu trữ của dự án Universal Dependencies (không cần tải thủ công bằng tay).
4. Chạy tuần tự các Cell còn lại từ trên xuống dưới để quan sát kết quả phân tích.

## Nội dung chính trong Demo

Demo bao gồm:

- **Phân tích & Trực quan hóa:** Dùng `spaCy` để phân tách câu, trích xuất các thành phần Head - Dependent và vẽ cây cú pháp để quan sát tính Projectivity (không có cung cắt chéo).
- **Sử dụng Real Dataset:** Load tập dữ liệu *Universal Dependencies (English Web Treebank)* với định dạng chuẩn `CoNLL-U`.
- **Đánh giá mô hình:** Chạy thuật toán để so sánh nhãn dự đoán của mô hình với nhãn chuẩn (Gold Standard), từ đó xuất ra 2 chỉ số đo lường hiệu suất quan trọng nhất:
  - **UAS** (Unlabeled Attachment Score)
  - **LAS** (Labeled Attachment Score)
- **Biểu diễn Graph-based:** Sử dụng `NetworkX` mô phỏng cây phụ thuộc dưới dạng Đồ thị có hướng (Directed Graph), giúp hình dung rõ hơn cách các thuật toán tìm kiếm cây khung nhỏ nhất (như Maximum Spanning Tree) hoạt động.

## Thư viện cốt lõi sử dụng
- `spaCy`: Cung cấp Neural Transition-based Parser.
- `conllu`: Xử lý tập tin dữ liệu dạng CoNLL-U.
- `NetworkX` & `Matplotlib`: Xây dựng cấu trúc đồ thị và trực quan hoá.