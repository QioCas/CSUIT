# Demo Hỏi Đáp trên Tài Liệu bằng LLM (Document QA Pipeline)

Dự án này chứa Jupyter Notebook (`NLP_C11.ipynb`) triển khai một hệ thống Hỏi đáp trên tài liệu theo kiến trúc **RAG (Retrieval-Augmented Generation)**. Mô hình cho phép người dùng đặt câu hỏi và nhận câu trả lời dựa trên nội dung của một tài liệu văn bản được cung cấp sẵn.

Luồng xử lý (Pipeline) của hệ thống bao gồm:
1. **Đưa tài liệu vào hệ thống (Document Ingestion):** Đọc file văn bản đầu vào bằng `TextLoader`.
2. **Chia nhỏ văn bản (Chunking):** Cắt tài liệu dài thành các đoạn nhỏ bằng `RecursiveCharacterTextSplitter`.
3. **Vector hóa (Embedding):** Dùng `HuggingFaceEmbeddings` với model `BAAI/bge-m3` để chuyển chunk thành vector ngữ nghĩa.
4. **Lưu trữ & Tìm kiếm (Vector Database):** Sử dụng `QdrantVectorStore` để lưu vector và truy xuất các đoạn liên quan nhất.
5. **Sinh câu trả lời (LLM Generation):** Ghép các đoạn truy xuất được làm ngữ cảnh cho mô hình `TinyLlama/TinyLlama-1.1B-Chat-v1.0` để sinh đáp án cuối cùng.

## 1. Yêu cầu cài đặt (Dependencies)

Notebook này được viết bằng Python 3 và sử dụng các thư viện chính sau:

- `faiss-cpu`
- `langchain`
- `langchain-core`
- `langchain-community`
- `langchain-text-splitters`
- `langchain-huggingface`
- `langchain-qdrant`
- `transformers`

Lệnh cài đặt nhanh trong Notebook:
```bash
!pip install faiss-cpu
!pip install -q langchain-google-genai
!pip install -q langchain langchain-core langchain-google-genai
```

## 2. Hướng dẫn sử dụng

### Chuẩn bị
1. Đặt file tài liệu văn bản cần hỏi đáp vào cùng thư mục với notebook.
2. Đảm bảo file có tên đúng như trong cell load dữ liệu, hiện tại là `README.txt`.
3. Nếu tên file khác, sửa lại tham số truyền vào `TextLoader`.

### Cách chạy

#### Cách 1: Chạy bằng Jupyter Notebook
1. Mở terminal tại thư mục chứa notebook.
2. Gõ lệnh:
   ```bash
   jupyter notebook
   ```
3. Mở `NLP_C11.ipynb` trong giao diện web.
4. Chạy lần lượt các cell từ trên xuống dưới.
5. Xem câu trả lời và các nguồn được truy xuất ở cuối notebook.

#### Cách 2: Chạy bằng VS Code
1. Mở thư mục dự án trong VS Code.
2. Cài extension Jupyter nếu chưa có.
3. Mở file `NLP_C11.ipynb`.
4. Chọn đúng Python kernel đang có các thư viện cần thiết.
5. Chạy toàn bộ notebook.

#### Cách 3: Chạy trên Google Colab
1. Tải notebook lên Colab.
2. Upload thêm file tài liệu đầu vào lên session.
3. Sửa lại tên file trong cell load dữ liệu nếu cần.
4. Chạy toàn bộ notebook để tạo embedding, lưu vector và sinh câu trả lời.

## 3. Mô tả ngắn về pipeline

Notebook này hoạt động theo thứ tự:
- tải tài liệu,
- tách văn bản thành các đoạn nhỏ,
- chuyển các đoạn thành vector,
- lưu vector vào Qdrant,
- truy xuất các đoạn phù hợp với câu hỏi,
- dùng prompt ép mô hình trả lời chỉ dựa trên tài liệu.

## 4. Ghi chú

Notebook hiện đang dùng câu hỏi mẫu:
```python
question = "What is scikit-learn?"
```
Bạn có thể thay câu hỏi này bằng câu hỏi khác để kiểm tra khả năng truy xuất và sinh câu trả lời của hệ thống.
