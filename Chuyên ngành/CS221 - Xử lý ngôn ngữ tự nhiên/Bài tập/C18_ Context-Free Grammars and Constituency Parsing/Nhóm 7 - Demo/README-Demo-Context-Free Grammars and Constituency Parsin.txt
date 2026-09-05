# NLP Demo - Chapter 18: Context-Free Grammars & Constituency Parsing

Dữ liệu thực tế được sử dụng là bộ dữ liệu **ATIS (Airline Travel Information System)**.

## Nội dung Demo

Notebook được chia thành 6 phần chính:
1. **Khám phá dữ liệu ATIS:** Tải và xem trước các câu truy vấn đặt vé máy bay thực tế.
2. **Context-Free Grammars (CFG):** Định nghĩa hệ thống văn phạm (Grammar & Lexicon) thủ công.
3. **Parse Tree Generation:** Sinh và vẽ cây phân tích cú pháp cho một câu cụ thể.
4. **Sự nhập nhằng cấu trúc (Structural Ambiguity):** Demo hiện tượng PP-attachment ambiguity khiến một câu sinh ra nhiều cây cú pháp.
5. **Chomsky Normal Form (CNF) & CKY Parsing:** Kiểm tra chuẩn CNF và chạy thuật toán phân tích cú pháp theo cơ chế Bottom-up (CKY-style).
6. **Neural Constituency Parsing:** Ứng dụng mô hình Deep Learning hiện đại (`stanza` của Stanford) để phân tích cú pháp mà không cần viết luật thủ công.

## Cài đặt (Prerequisites)

Demo sử dụng Python. Cần cài đặt các thư viện sau trước khi chạy:

```bash
pip install pandas nltk stanza svgling

## Cách chạy Demo
1. Clone thư mục này hoặc tạo một file demo_parsing.ipynb và dán các cell code vào.
2. Mở file bằng Jupyter Notebook, VS Code hoặc upload lên Google Colab.
3. Chạy tuần tự các ô code (cells) từ trên xuống dưới.

## Lưu ý
Tập dữ liệu ATIS được code tự động tải qua link raw trên internet, không cần phải download data thủ công.