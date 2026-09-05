# Demo Hỏi Đáp trên Tài Liệu bằng LLM (Document QA Pipeline)

Dự án này chứa Jupyter Notebook (`demo_qa_llm_tu_tai_lieu.ipynb`) triển khai một hệ thống Hỏi đáp trên tài liệu dựa trên kiến trúc **RAG (Retrieval-Augmented Generation)**. Mô hình cho phép người dùng đặt câu hỏi và nhận câu trả lời dựa trên nội dung của một tài liệu văn bản cung cấp sẵn.

Luồng xử lý (Pipeline) của hệ thống bao gồm:
1. **Đọc tài liệu (Document Ingestion):** Hỗ trợ trích xuất nội dung từ các định dạng `.txt`, `.pdf`, `.docx`.
2. **Chia nhỏ văn bản (Chunking):** Cắt tài liệu dài thành các đoạn văn bản (chunks) có kích thước phù hợp với giới hạn của mô hình.
3. **Vector hóa (Embedding):** Sử dụng mô hình `sentence-transformers` (`all-MiniLM-L6-v2`) để chuyển đổi chunks thành các vector ngữ nghĩa.
4. **Lưu trữ & Tìm kiếm (Vector Database):** Sử dụng thư viện `FAISS` để lưu trữ vector và truy xuất `top_k` đoạn văn bản liên quan nhất đến câu hỏi của người dùng.
5. **Sinh câu trả lời (LLM Generation):** Cung cấp các đoạn văn bản truy xuất được làm ngữ cảnh (Context) cho mô hình LLM (`google/flan-t5-base`) để tổng hợp và sinh ra câu trả lời cuối cùng.

## 1. Yêu cầu cài đặt (Dependencies)

Các Notebook được viết bằng Python 3. Bạn nên sử dụng môi trường ảo (Conda, Virtualenv) và cài đặt các thư viện thông qua `pip`.

Các thư viện chính cần thiết:
- `transformers` (Hỗ trợ tải và chạy LLM)
- `sentence-transformers` (Hỗ trợ tạo Word/Sentence Embedding)
- `faiss-cpu` (Cơ sở dữ liệu Vector)
- `pypdf` (Để đọc file `.pdf`)
- `python-docx` (Để đọc file `.docx`)

*Lệnh cài đặt nhanh trong Notebook: `!pip install transformers sentence-transformers faiss-cpu pypdf python-docx`*

## 2. Hướng dẫn sử dụng
### Chuẩn bị
1. Đặt file tài liệu bạn muốn hỏi đáp (ví dụ: `tailieu.pdf` hoặc `data.txt`) vào cùng thư mục với notebook.
2. Mở notebook và sửa đổi biến `DOCUMENT_PATH` trỏ tới đúng tên file của bạn.

### Chọn cách chạy

#### Cách 1: Chạy bằng Jupyter Notebook (Môi trường Web)
1. Mở terminal và trỏ đến thư mục chứa bài code này.
2. Gõ lệnh:
   ```bash
   jupyter notebook
3. Một giao diện web tại localhost:8888 sẽ mở lên, bạn click chuột trực tiếp để mở file demo_qa_llm_tu_tai_lieu.ipynb
4. Bấm Run -> Run All Cells trên thanh menu để hệ thống lần lượt cài đặt, tải LLM và thiết lập cơ sở dữ liệu.
5. Ở các cell cuối, gọi hàm ask('Câu hỏi của bạn ở đây') để tương tác.

#### Cách 2: Chạy bằng Visual Studio Code (VS Code) / Pycharm
1. Đảm bảo VS Code đã cài đặt extension Jupyter.
2. Mở dự án trong VS Code. Double click để mở demo_qa_llm_tu_tai_lieu.ipynb.
3. Phía góc phải trên cùng màn hình file mã, Select Kernel và chọn đúng môi trường ảo Python bạn đã thực thi cài đặt thư viện ở bước 1.
4. Bấm nút Run All ở thanh công cụ của Notebook và chờ kết quả in xuất ra ở các cell cuối của file.

#### Cách 3: Đẩy thẳng lên Google Colab
1. Truy cập Google Colab.
2. Chọn tab Upload và tải file demo_qa_llm_tu_tai_lieu.ipynb lên.
3. Upload thêm file tài liệu (.pdf, .txt, .docx) của bạn lên session của Colab (bên thanh công cụ bên trái).
4. Cập nhật lại đường dẫn DOCUMENT_PATH.
5. Bấm Runtime -> Run all (hoặc Ctrl + F9) để tận dụng môi trường máy chủ của Google thực thi mô hình.