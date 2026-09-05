# PretrainLLM.ipynb

## Giới thiệu
`PretrainLLM.ipynb` là một mô hình LLM đơn giản được xây dựng để minh họa quy trình pretrain cơ bản.

Mô hình:
- Sử dụng **word-level tokenization**
- Khởi tạo embedding từ **Word2Vec (300d)**
- Kiến trúc đơn giản: **Embedding + Linear**
- Huấn luyện theo bài toán **next token prediction**

Mục tiêu chính là giúp hiểu pipeline của một LLM từ dữ liệu → huấn luyện → sinh văn bản.

---

## Pipeline

Text  
→ Tokenization (word-level)  
→ Encode thành index  
→ Train/Val split  
→ Batching (sequence length = 32)  
→ Word2Vec Embedding  
→ Model (Embedding → Linear → Softmax)  
→ Training (Next Token Prediction)  
→ Text Generation


# DataAugmentation

## Giới thiệu
Folder `DataAugmentation` chứa code để tăng cường dữ liệu cho bài toán phân loại:
- Xác định một câu có phải **conspiracy** hay không (`Yes` / `No`)

Phương pháp:
- Sử dụng **few-shot prompting** với LLM (Groq API) để sinh thêm dữ liệu mới

Yêu cầu:
- Tạo tài khoản Groq
- Thêm API key vào file `.env`:

GROQ_API_KEY=your_api_key_here


---

## Pipeline

JSONL data  
→ Filter label (`Yes` / `No`)  
→ Few-shot Prompt Construction  
→ LLM Inference (Groq API)  
→ Retry nếu lỗi  
→ Generate new text  
→ Gán label tương ứng  
→ Append vào dataset mới  
→ Autosave theo batch  
→ Final augmented dataset

---

## Hiệu năng

Áp dụng data augmentation giúp cải thiện nhẹ hiệu năng:

| Aug. size | F1 (No) | F1 (Yes) | F1 (weighted) |
|----------|--------|----------|---------------|
| 0        | 77.66  | 74.90    | 76.38         |
| 850      | 77.14  | 75.80    | 76.52         |

→ Nhận xét:
- F1 lớp **Yes** tăng đáng kể
- F1 weighted tăng nhẹ
- Tổng thể: augmentation có tác dụng nhưng chưa quá mạnh

---

## Nhận xét

- Bài toán **conspiracy detection** có tính chất khó do:
  - Phụ thuộc ngữ cảnh và sắc thái ngôn ngữ
  - Ranh giới giữa các lớp không rõ ràng

- Data augmentation bằng LLM:
  - Có thể cải thiện độ đa dạng dữ liệu
  - Nhưng cũng dễ sinh dữ liệu chưa đủ khác biệt hoặc lệch phân phối

→ Do đó, việc cải thiện hiệu năng chỉ ở mức nhẹ là hợp lý.