Demo Chương 17: Sequence Labeling (Jurafsky & Martin)

Ứng dụng: Gán nhãn Từ loại (POS) và Nhận dạng Thực thể (NER) trên tiếng Việt

📖 Tổng quan Source Code

Dự án này là bản cài đặt thực hành dựa trên kiến thức của Chương 17: Sequence Labeling trong giáo trình Speech and Language Processing (Jurafsky & Martin). Dự án tập trung vào việc giải quyết bài toán xử lý ngôn ngữ tự nhiên mức độ từ (token-level) cho tiếng Việt, cụ thể là phân loại từ (POS Tagging) và trích xuất thông tin (NER).

Source code (CS221_Chapter17_Demo.ipynb) được chia thành các phần chính:

Phần 1 & 2: Tiền xử lý dữ liệu - Đọc văn bản thô từ bộ dữ liệu VLSP 2018 (Restaurant Sentiment). Do dữ liệu gốc không có nhãn mức độ từ, dự án sử dụng underthesea như một công cụ Oracle để mồi nhãn POS/NER (BIO format), tạo thành tập Ground Truth để huấn luyện các mô hình.

Phần 3: Baseline Model (Mục 17.2) - Thuật toán cơ sở, gán nhãn dựa trên tần suất xuất hiện cao nhất của từ (Most Frequent Class) trong tập huấn luyện.

Phần 4: Hidden Markov Model (HMM) & Viterbi Decoder (Mục 17.4) - Xây dựng mô hình Generative với ma trận Transition và Emission. Đặc biệt: Đã tích hợp thuật toán Laplace (Add-k) Smoothing để giải quyết triệt để lỗi OOV (từ chưa biết) và underflow xác suất.

Phần 5: Conditional Random Fields (CRF) (Mục 17.5) - Xây dựng mô hình Discriminative với bộ trích xuất đặc trưng (Feature Extraction) bao gồm: định dạng chữ, tiền tố, hậu tố, và ngữ cảnh lân cận (sliding window).

Phần 6: Đánh giá & Suy luận (Mục 17.6) - Đo lường POS Tagging bằng Accuracy, NER bằng F1-Score (thông qua seqeval). Tích hợp tính năng Interactive Input cho phép người dùng nhập câu tùy ý và xem kết quả giải mã trực tiếp.

📂 Cấu trúc thư mục (Directory Structure)

Để mã nguồn chạy thành công (nếu chạy local), bạn cần tổ chức thư mục dự án chính xác như sau:

CS221_Project_Chap17/
│
├── CS221_Chapter17_Demo.ipynb                # File Source Code (Jupyter Notebook)
│
├── 1-VLSP2018-SA-Restaurant-train (7-3-2018).txt  # Dữ liệu Train thô
└── 3-VLSP2018-SA-Restaurant-test (8-3-2018).txt   # Dữ liệu Test thô


(Lưu ý: Nếu không tải được file TXT lên, source code đã tích hợp sẵn cơ chế Fallback Mock Data (dữ liệu giả lập) để đảm bảo file chạy không bị gián đoạn).

⚙️ Hướng dẫn Cài đặt (Setup)

Dự án sử dụng các thư viện phổ biến trong học máy học và xử lý ngôn ngữ tiếng Việt. Bạn cần cài đặt chúng thông qua pip trong Terminal hoặc chạy trực tiếp Cell đầu tiên trong Notebook:

pip install underthesea sklearn-crfsuite seqeval


underthesea: Tiền xử lý và tạo nhãn mồi (Tokenize, POS, NER) cho tiếng Việt.

sklearn-crfsuite: Thư viện lõi để huấn luyện mô hình Conditional Random Fields.

seqeval: Đánh giá hiệu năng NER theo chuẩn BIO.

🚀 Hướng dẫn Chạy Source Code (Execution)

Bạn nên ưu tiên chạy dự án này trên Google Colab để tránh xung đột môi trường Python.

Chạy trên Google Colab (Khuyên dùng)

Truy cập Google Colab.

Chọn File > Upload notebook và tải lên file CS221_Chapter17_Demo.ipynb.

Nhìn sang thanh menu bên trái, bấm vào biểu tượng Thư mục (Files).

Bấm biểu tượng Upload (tải lên) và chọn 2 file .txt (Train, Test) của tập VLSP 2018 Restaurant. (Đợi vòng tròn upload quay xong).

Trên thanh Menu trên cùng, chọn Runtime > Run all (hoặc bấm Ctrl + F9).

Cuộn xuống dưới cùng để tương tác với ô nhập liệu (Interactive Input).

📊 Đọc hiểu Kết quả (Expected Output)

Khi bạn cuộn xuống cuối file Notebook, bạn sẽ thấy 2 phần đánh giá chính và 1 phần kiểm thử tương tác:

1. Đánh giá POS Tagging (HMM)

Đánh giá độ chính xác gán nhãn từ loại trên toàn bộ số lượng token của tập Test.

=== ĐÁNH GIÁ MÔ HÌNH HMM (POS TAGGING) ===
Độ chính xác (Accuracy) trên toàn bộ tập Test: 83.70%


2. Đánh giá NER (CRF)

Sử dụng một câu tiếng Việt tiêu chuẩn (có chứa thực thể) để demo sức mạnh của CRF:

=== ĐÁNH GIÁ MÔ HÌNH CRF (NER) ===
Word                 | True NER   | CRF NER   
---------------------------------------------
Trường học           | O          | O         
Đại học              | B-LOC      | B-LOC     
Bách Khoa            | I-LOC      | I-LOC     
...                  | ...        | ...
Nam                  | B-PER      | B-PER 


3. Tương tác trực tiếp (Interactive CLI)

Ở Cell cuối cùng, khi hộp thoại hiện ra, bạn nhập một câu bất kỳ (Ví dụ: "Tôi là Cáp Kim Hải Anh, học tại ĐHQG-HCM"). Mô hình sẽ dùng underthesea để Tokenize, sau đó nạp vào HMM để đoán POS và nạp vào CRF để đoán NER, kết quả được ánh xạ thành bảng trực quan.

Nhập câu bạn muốn kiểm thử: Tôi là Cáp Kim Hải Anh, học tại Trường Đại học Công nghệ thông tin - ĐHQG-HCM

==================================================
KẾT QUẢ DỰ ĐOÁN SEQUENCE LABELING
==================================================
Từ (Word)            | HMM (POS)    | CRF (NER)   
--------------------------------------------------
Tôi                  | P            | O           
là                   | V            | O           
Cáp Kim Hải Anh      | T            | B-LOC       
...
