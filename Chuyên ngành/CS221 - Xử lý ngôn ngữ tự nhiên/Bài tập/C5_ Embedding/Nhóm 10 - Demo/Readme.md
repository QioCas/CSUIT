1. Mục tiêu bài thực hành
- Làm quen với thư viện sentence transformers để xử lý Vector embedding 
- Finetune mô hình trên một bộ dataset từ trên Kaggle 
- Xây dựng hệ thống tìm kiếm ngữ nghĩa, tìm ra bài báo có nội dung gần hoặc tương tự như query 

2. Cách chạy lại file  
- Thực hành trên Google Colab 
- Download và unzip dataset từ trên kaggle 
- Để dataset hoặc code sử dụng đúng path
- Chạy lần lượt các cell 

3. Nội dung thực hành 
- Lựa chọn mô hình: Sử dụng mô hình tiền huấn luyện chuyên dụng cho tiếng Việt (bkai-foundation-models) để làm nền tảng.
- Định nghĩa hàm mất mát: Sử dụng Multiple Negatives Ranking Loss - kỹ thuật giúp mô hình phân biệt tốt hơn giữa các cặp câu tương đồng và khác biệt.
- Fine-tuning: Chạy quy trình huấn luyện trên tập dữ liệu mẫu để mô hình thích nghi với bối cảnh và từ vựng của bài báo.











