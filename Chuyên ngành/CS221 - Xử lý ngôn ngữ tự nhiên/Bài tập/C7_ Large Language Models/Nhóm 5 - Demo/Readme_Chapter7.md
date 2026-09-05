Demo Chương 7: Large Language Models (LLMs)

Chương trình demo: In-context Learning & Prompting cho Aspect-Based Sentiment Analysis

📖 Giới thiệu (Introduction)

Dự nn này là bản cài đặt thực hành từ con số 0 (from scratch) các kiến thức cốt lõi của Chương 7: Large Language Models trong giáo trình Speech and Language Processing (Jurafsky & Martin).

Mục tiêu của dự án là minh họa sự dịch chuyển mô hình (Paradigm Shift) của Kỷ nguyên AI tạo sinh:
Thay vì xây dựng các mô hình phân loại (classifier) chuyên biệt để đưa ra một nhãn (Label), chúng ta xây dựng một Mô hình Ngôn ngữ Tự hồi quy (Autoregressive Language Model) dựa trên kiến trúc Transformer. Mô hình này chỉ làm duy nhất một nhiệm vụ: Dự đoán từ tiếp theo. Mọi bài toán phân tích cảm xúc (Sentiment Analysis) trên tập dữ liệu VLSP 2018 đều được giải quyết thông qua kỹ thuật Prompting và sinh văn bản tự nhiên.

🧠 Mô tả Source Code (Code Overview)

Mã nguồn Notebook Jupyter được thiết kế tối giản, loại bỏ các thư viện rườm rà để người học có thể nhìn thấu bản chất toán học bên trong. Code được chia làm 5 phần chính:

Text-to-Text Formatting: Chuyển đổi dữ liệu thô thành các chuỗi văn bản hoàn chỉnh.
Ví dụ: "Review: Đồ ăn ngon . Aspect: Ẩm thực => Sentiment: TICH_CUC <EOS>"

Autoregressive Dataset: Xử lý dữ liệu thành Input (X) và Target (Y), trong đó Y chính là X được dịch sang phải 1 vị trí (shifted).

Kiến trúc Transformer Decoder: Cài đặt mạng Transformer kết hợp Causal Mask (Mặt nạ nhân quả). Kỹ thuật này ép mô hình khi dự đoán từ ở vị trí t chỉ được phép sử dụng thông tin từ vị trí 1 đến t, không được "nhìn lén" tương lai.

Pre-training (Huấn luyện): Huấn luyện mô hình liên tục dự đoán từ tiếp theo trên tập dữ liệu. Đánh giá chất lượng mô hình thông qua chỉ số Perplexity (Sự bối rối).

Prompting (Sinh văn bản): Áp dụng In-context Learning. Cung cấp cho mô hình một đoạn Prompt và sử dụng thuật toán Greedy Decoding để mô hình tự động sinh ra câu trả lời chứa nhãn cảm xúc.

📂 Cấu trúc thư mục (Directory Structure)

Để code chạy thành công, hãy đảm bảo thư mục dự án của bạn được tổ chức như sau:

LLM_Chapter7_Project/
│
├── CS221_Chapter7_Demo.ipynb                      # File Source Code 
│
├── 1-VLSP2018-SA-Restaurant-train (7-3-2018).txt  # Dữ liệu Train
├── 2-VLSP2018-SA-Restaurant-dev (7-3-2018).txt    # Dữ liệu Dev (Validation)
└── 3-VLSP2018-SA-Restaurant-test (8-3-2018).txt   # Dữ liệu Test


(Nếu muốn chạy dữ liệu Hotel, chỉ cần copy 3 file Hotel vào thư mục và đổi tên file đọc trong code).

⚙️ Hướng dẫn Cài đặt (Setup)

Dự án yêu cầu môi trường Python 3.8+. Mở Terminal hoặc Command Prompt và chạy lệnh sau để cài đặt thư viện PyTorch (thư viện tính toán lõi):

pip install torch


🚀 Hướng dẫn Chạy Demo (Execution)

Cách 1: Chạy trên Google Colab (Khuyên dùng)

Truy cập Google Colab.

Chọn Upload và tải lên file mã nguồn demo_chap7_llm_absa.py (hoặc copy toàn bộ code dán vào một Notebook mới).

Ở menu bên trái, chọn biểu tượng Files (Thư mục). Tải lên 3 file dữ liệu .txt của tập VLSP 2018. (Chờ quá trình tải lên hoàn tất 100%).

Bấm Runtime > Run all (Hoặc chạy từng Cell nếu dùng dạng Notebook) để quan sát mô hình học ngôn ngữ.

Cách 2: Chạy trên máy tính cá nhân (VS Code / Terminal)

Mở Terminal / Command Prompt, di chuyển (cd) vào thư mục LLM_Chapter7_Project.

Chạy lệnh:

python CS221_Chapter19_Demo.ipynb


📊 Kết quả mong đợi (Expected Output)

Tại bước cuối cùng của chương trình (Bước 5), LLM sẽ tự động trả lời các câu hỏi dựa trên Prompting thay vì dùng các hàm phân loại truyền thống.

===========================================================================
 DEMO: SỬ DỤNG PROMPTING ĐỂ THỰC HIỆN SENTIMENT ANALYSIS
===========================================================================
[PROMPT GỬI VÀO LLM] : 'Review: đồ ăn ở đây ngon tuyệt vời . Aspect: food#quality => Sentiment:'
[LLM TỰ ĐỘNG SINH]  : ---> [TICH_CUC]
---------------------------------------------------------------------------
[PROMPT GỬI VÀO LLM] : 'Review: nhân viên phục vụ cực kỳ chậm chạp và thái độ . Aspect: service#general => Sentiment:'
[LLM TỰ ĐỘNG SINH]  : ---> [TIEU_CUC]
---------------------------------------------------------------------------