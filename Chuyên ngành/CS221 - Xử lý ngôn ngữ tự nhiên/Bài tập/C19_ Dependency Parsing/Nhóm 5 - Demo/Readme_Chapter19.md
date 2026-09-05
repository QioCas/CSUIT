Demo Chương 19: Dependency Parsing

Phân tích Cú pháp vào Bài toán Aspect-Based Sentiment Analysis (ABSA)

📖 Giới thiệu (Introduction)

Dự án này là bản cài đặt thực hành các thuật toán từ Chương 19: Dependency Parsing trong cuốn sách Speech and Language Processing (Jurafsky & Martin).

Mục tiêu của dự án là minh họa cách máy tính hiểu được cấu trúc ngữ pháp (Syntax) của một câu Tiếng Việt thông qua việc xây dựng Cây Cú pháp Phụ thuộc (Dependency Tree). Trong bài toán phân tích cảm xúc (như VLSP 2018), việc biết được tính từ nào bổ nghĩa cho danh từ nào (Ví dụ: "ngon" bổ nghĩa cho "đồ_ăn") là yếu tố quyết định để mô hình không gán nhầm cảm xúc.

Dự án này mô phỏng một Hệ thống Phân tích Cú pháp dựa trên Dịch chuyển (Transition-Based Parsing) sử dụng Mạng Neural (theo kiến trúc Chen & Manning 2014).

🧠 Kiến trúc Mã nguồn (Source Code Architecture)

Mã nguồn Jupyter Notebook (CS221_Chapter19_Demo.ipynb) được thiết kế bám sát từng mục trong sách, bao gồm các phần cốt lõi sau:

Mini-Treebank: Giả lập dữ liệu huấn luyện bằng cách tự tay chú thích cấu trúc cây phụ thuộc cho một số câu mẫu từ bộ VLSP 2018 (mỗi từ đều trỏ về Head của nó).

Oracle Algorithm (Tiên tri): Thuật toán mô phỏng hệ thống Arc-Standard. Thuật toán "nhìn trộm" cây chuẩn để vạch ra lộ trình các hành động đúng đắn nhất: SHIFT (Đẩy từ vào Stack), LEFT-ARC (Tạo liên kết trái), RIGHT-ARC (Tạo liên kết phải).

Neural Dependency Parser: Xây dựng Mạng Feedforward Neural Network bằng PyTorch. Hệ thống trích xuất đặc trưng từ 2 từ trên đỉnh Stack và 2 từ đầu Buffer để đưa ra dự đoán hành động tiếp theo.

Training (Huấn luyện): Huấn luyện mạng Neural học cách bắt chước ông "Oracle".

Inference (Phân tích câu mới): Đưa một câu hoàn toàn mới (VD: "Đồ_ăn của quán rất ngon") vào "cỗ máy" để mô hình tự động thực hiện các hành động SHIFT/ARC và vẽ ra cây cú pháp hoàn chỉnh.

📂 Cấu trúc thư mục (Directory Structure)

Để code chạy thành công, hãy đặt file Jupyter Notebook trong thư mục dự án của bạn:

CS221_Chapter19_Project/
│
└── CS221_Chapter19_Demo.ipynb       # File Source Code chính


(Lưu ý: Mã nguồn đã tích hợp sẵn tập dữ liệu Mini-Treebank bên trong, nên bạn không cần tải thêm bất kỳ file .txt nào từ bên ngoài).

⚙️ Hướng dẫn Cài đặt (Setup)

Môi trường yêu cầu Python 3.8+. Mở Terminal hoặc Command Prompt và cài đặt các thư viện lõi thông qua pip:

pip install torch jupyter


🚀 Hướng dẫn Chạy Demo (Execution)

Cách 1: Chạy trên Google Colab (Khuyên dùng)

Đây là cách nhanh nhất và không lo lỗi môi trường cài đặt.

Truy cập Google Colab.

Chọn File > Upload notebook và tải lên file CS221_Chapter19_Demo.ipynb.

Trên thanh Menu trên cùng, chọn Runtime > Run all (hoặc bấm Ctrl + F9).

Kéo xuống dưới cùng để xem cỗ máy tự động phân tích ngữ pháp của câu.

Cách 2: Chạy trực tiếp trên máy tính (Local)

Mở Terminal / Command Prompt, di chuyển (cd) vào thư mục CS221_Chapter19_Project.

Gõ lệnh khởi động Jupyter Notebook:

jupyter notebook


Trình duyệt web sẽ tự động mở ra. Bạn click chọn file CS221_Chapter19_Demo.ipynb.

Trên thanh công cụ của Jupyter, chọn Cell > Run All (hoặc Kernel > Restart & Run All) để thực thi toàn bộ mã nguồn.

📊 Kết quả mong đợi (Expected Output)

Tại bước cuối cùng (Inference), bạn sẽ thấy cỗ máy mô phỏng quá trình hoạt động của hệ thống Arc-Standard để xử lý câu "Đồ_ăn của quán rất ngon" và in ra cây phụ thuộc cuối cùng:

============================================================
 DEMO: PHÂN TÍCH CÚ PHÁP CÂU MỚI (INFERENCE)
============================================================
Câu cần phân tích: Đồ_ăn của quán rất ngon

Bước 1: SHIFT từ 'Đồ_ăn' vào Stack
Bước 2: RIGHT-ARC (<ROOT> -> Đồ_ăn)
Bước 3: SHIFT từ 'của' vào Stack
Bước 4: RIGHT-ARC (<ROOT> -> của)
...
Bước 9: LEFT-ARC (ngon -> quán)
Bước 10: RIGHT-ARC (<ROOT> -> ngon)

=> KẾT QUẢ CÂY PHỤ THUỘC (DEPENDENCY TREE):
  [<ROOT>] -----> [Đồ_ăn]
  [<ROOT>] -----> [của]
  [ngon] -----> [rất]
  ...


Giải thích: Kết quả này chứng minh mạng Neural đã học được cách định tuyến thông minh (nhận diện tính từ "ngon" có mối liên kết với các từ khác trong câu), cung cấp thông tin cú pháp quý giá để giải quyết các bài toán ngữ nghĩa nâng cao hơn!

Nhóm 5 - Lớp CS221.Q21.KHTN