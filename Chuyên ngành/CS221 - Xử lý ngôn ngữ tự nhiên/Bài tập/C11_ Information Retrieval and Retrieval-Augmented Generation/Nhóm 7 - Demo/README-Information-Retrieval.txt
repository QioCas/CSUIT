# Demo: Information Retrieval & Retrieval-Augmented Generation (RAG)

## Nội dung chính
Demo bao gồm 3 phần chính:
1. **Sparse Retrieval (Tìm kiếm thưa):** Trích xuất tài liệu dựa trên từ khóa chính xác sử dụng thuật toán `BM25`.
2. **Dense Retrieval (Tìm kiếm dày):** Tìm kiếm theo ngữ nghĩa (Semantic Search) sử dụng Bi-encoder (`all-MiniLM-L6-v2`) kết hợp với `FAISS` để tối ưu tốc độ truy xuất.
3. **Retrieval-Augmented Generation (RAG):** Kết hợp kết quả tìm kiếm với Large Language Model (`google/flan-t5-base`) để sinh câu trả lời tự nhiên, chính xác, giảm thiểu "ảo giác" (hallucination).

## Tập dữ liệu (Dataset)
Demo sử dụng tập dữ liệu **Wikipedia Movie Plots** (chứa cốt truyện của các bộ phim).
- **Link tải:** [Kaggle - Wikipedia Movie Plots](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots)
- **File yêu cầu:** `wiki_movie_plots_deduped.csv`

## Cài đặt & Chuẩn bị 

1. Clone repository hoặc tải file `.ipynb` về máy.
2. Cài đặt các thư viện Python cần thiết:
   ```bash
   pip install transformers sentence-transformers faiss-cpu rank_bm25 pandas torch numpy
3. Đảm bảo file dữ liệu wiki_movie_plots_deduped.csv được đặt cùng thư mục với file Notebook (hoặc upload trực tiếp lên môi trường nếu dùng Google Colab)

## Cách chạy 
1. Mở file Notebook (.ipynb) bằng Jupyter Notebook hoặc tải lên Google Colab.
2. Nếu sử dụng Google Colab hoặc Kaggle, bật GPU (T4 GPU) trong phần Runtime > Change runtime type để tăng tốc độ thực thi.
3. Chạy lần lượt các ô từ trên xuống dưới:
Tải dữ liệu.
Trải nghiệm thử BM25 và Dense Search.
Thử nghiệm đặt câu hỏi bằng RAG pipeline.