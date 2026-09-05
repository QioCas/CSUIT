# CHƯƠNG 11: RETRIEVAL-AUGMENTED GENERATION (RAG)

**Nhóm đề tài: Nhóm 5**

Đây là bản demo hoàn chỉnh cho kiến trúc **Retrieval-Augmented Generation (RAG)** được xây dựng theo nội dung cốt lõi của **Chương 11** trong *Speech and Language Processing (SLP3)* của Daniel Jurafsky và James H. Martin.

## Tổng Quan

Mục tiêu của dự án là mô phỏng một hệ thống hỏi đáp thực tế có khả năng:

- truy xuất tri thức từ kho dữ liệu bên ngoài thay vì chỉ dựa vào tri thức nội tại của mô hình sinh;
- giảm hiện tượng hallucination bằng cách ràng buộc câu trả lời vào ngữ cảnh truy xuất được;
- minh họa đầy đủ pipeline RAG gồm retrieval, ranking, prompt construction và generation.

Hệ thống phù hợp cho các bài toán hỏi đáp factoid, demo học thuật, và thử nghiệm quy trình làm việc với LLM theo hướng grounded generation.

## Kiến Trúc Hệ Thống

Pipeline của notebook gồm 5 bước chính:

1. Cài đặt và khởi tạo thư viện.
2. Tải dataset benchmark và xây dựng chỉ mục vector FAISS.
3. Định nghĩa tầng truy xuất và tạo prompt.
4. Khởi tạo mô hình sinh và luồng generate câu trả lời.
5. Chạy giao diện tương tác bằng `ipywidgets`.

### 1) Dataset và Tiền Xử Lý

- **Dataset:** WikiQA từ Microsoft.
- **Vai trò:** cung cấp câu hỏi và ngữ liệu Wikipedia để đánh giá truy xuất và sinh câu trả lời.
- **Kho tri thức:** notebook xử lý khoảng 3.000 phân đoạn văn bản Wikipedia làm knowledge base cho truy xuất.

### 2) Dense Retriever

- **Mô hình nhúng:** `sentence-transformers/all-MiniLM-L6-v2`.
- **Kiểu biểu diễn:** dense vectors cho cả câu hỏi và đoạn văn bản.
- **Chỉ mục:** FAISS `IndexFlatIP`.
- **Chuẩn hóa:** vector được chuẩn hóa $L_2$ để dùng inner product như cosine similarity.
- **Kết quả truy xuất:** lấy top $k = 5$ đoạn liên quan nhất cho mỗi truy vấn.

### 3) Generator LLM

- **Mô hình sinh:** Flan-T5-Base.
- **Kiến trúc:** encoder-decoder text-to-text, đã được instruction tuning.
- **Thiết lập chính:**
    - `temperature = 0.2` để giảm độ ngẫu nhiên;
    - `max_length = 128` để giữ câu trả lời ngắn gọn, phù hợp factoid QA.

### 4) Prompt Engineering

Prompt được thiết kế theo hướng instruction-based contextual prompting:

```text
Answer the question based on the provided context accurately.
If the context does not contain the answer, reply with 'unanswerable'.

Context:
- [Đoạn văn bản 1 trích xuất từ FAISS]
- [Đoạn văn bản 2 trích xuất từ FAISS]
- [Đoạn văn bản 3 trích xuất từ FAISS]
- [Đoạn văn bản 4 trích xuất từ FAISS]
- [Đoạn văn bản 5 trích xuất từ FAISS]

Question: [Câu hỏi nhập vào hệ thống]
Answer:
```

## Cấu Trúc Notebook

- **Bước 1:** Cài đặt và import thư viện.
- **Bước 2:** Tải dataset và xây dựng chỉ mục FAISS.
- **Bước 3:** Định nghĩa hàm truy xuất và tạo prompt.
- **Bước 4:** Khởi tạo mô hình sinh và hàm generate.
- **Bước 5:** Demo giao diện tương tác để nhập câu hỏi và xem câu trả lời.

## Yêu Cầu Môi Trường

- Python `>= 3.10`
- Google Colab hoặc môi trường Python có thể cài các gói từ Hugging Face Hub
- Kết nối Internet để tải model và dataset
- CPU là đủ để chạy demo; GPU chỉ giúp tăng tốc độ tải và suy luận

## Thư Viện Sử Dụng

- `datasets`: tải và quản lý WikiQA từ Hugging Face Hub.
- `sentence-transformers`: tạo embedding cho câu hỏi và văn bản.
- `faiss-cpu`: xây dựng và truy xuất chỉ mục vector.
- `transformers`: tải tokenizer và mô hình Flan-T5.
- `ipywidgets`: tạo giao diện nhập liệu tương tác trong notebook.

## Cài Đặt Trên Google Colab

1. Mở một notebook Python 3 mới trên [Google Colab](https://colab.research.google.com/).
2. Cài đặt các thư viện cần thiết:

```bash
!pip install -q transformers sentence-transformers faiss-cpu datasets ipywidgets
```

3. Mở file `C11_RAG.ipynb` và chạy tuần tự toàn bộ các cell.
4. Tại phần demo cuối notebook, nhập câu hỏi vào ô `ipywidgets` và nhấn nút **Chạy Hệ Thống RAG**.
5. Quan sát luồng xử lý từ truy xuất ngữ nghĩa đến sinh câu trả lời.

## Hướng Dẫn Chạy Nhanh

- Mở `C11_RAG.ipynb`.
- Chạy từ trên xuống dưới để tải model, dataset và dựng FAISS index.
- Ở cell giao diện, nhập truy vấn bất kỳ.
- Nhấn **Chạy Hệ Thống RAG** để nhận câu trả lời từ mô hình.

## Lưu Ý Khi Chạy

- Lần chạy đầu tiên có thể lâu hơn do phải tải model và dữ liệu từ Hugging Face.
- Nếu notebook báo thiếu thư viện, hãy chạy lại cell cài đặt ở Bước 1.
- Nếu dùng Colab, nên bật internet ổn định để tránh lỗi tải model hoặc dataset.
- Câu trả lời sẽ bám theo ngữ cảnh truy xuất; nếu không tìm thấy thông tin phù hợp, hệ thống có thể trả về `unanswerable`.

## Mục Tiêu Đầu Ra

Sau khi chạy xong notebook, bạn sẽ có một demo RAG hoàn chỉnh với các thành phần sau:

- kho tri thức Wikipedia đã được vector hóa;
- bộ truy xuất dense retrieval sử dụng FAISS;
- mô hình sinh Flan-T5-Base;
- giao diện nhập câu hỏi tương tác ngay trong notebook;
- cơ chế trả lời dựa trên ngữ cảnh truy xuất được.

## Tài Liệu Tham Khảo

- *Speech and Language Processing (SLP3)*, Chương 11: Retrieval-Augmented Generation.
- WikiQA benchmark dataset.
- FAISS, Sentence Transformers và Hugging Face Transformers.