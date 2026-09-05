# Demo trực quan hóa Attention của BERT

Dự án này chứa Jupyter Notebook (`NLP_C8_annotated.ipynb`) minh họa cách dùng mô hình **BERT** để lấy và trực quan hóa **attention** trên một câu đầu vào.

Notebook thực hiện các bước chính:
1. **Import thư viện:** Nạp `torch`, `matplotlib`, `seaborn` và `transformers`.
2. **Tải mô hình và tokenizer:** Sử dụng `bert-base-uncased`.
3. **Chuẩn bị câu đầu vào:** Đưa một câu mẫu vào để kiểm tra.
4. **Mã hóa token:** Chuyển câu thành tensor đầu vào cho BERT.
5. **Chạy mô hình:** Lấy đầu ra và attention của các layer.
6. **Trích xuất attention:** Chọn một layer và một head cụ thể.
7. **Vẽ heatmap:** Hiển thị mức độ chú ý giữa các token.

## 1. Yêu cầu cài đặt (Dependencies)

Notebook này được viết bằng Python 3. Bạn nên dùng môi trường ảo và cài đặt các thư viện sau:

- `torch`
- `transformers`
- `matplotlib`
- `seaborn`

Lệnh cài đặt nhanh:

```bash
pip install torch transformers matplotlib seaborn
```

## 2. Hướng dẫn sử dụng

### Chuẩn bị
1. Đặt file notebook `NLP_C8_annotated.ipynb` vào thư mục làm việc của bạn.
2. Mở notebook bằng Jupyter Notebook, VS Code hoặc Google Colab.
3. Chạy lần lượt từng cell từ trên xuống dưới.

### Kết quả mong đợi
Sau khi chạy xong, notebook sẽ hiển thị một heatmap attention cho câu mẫu `i love you`, giúp quan sát token nào đang chú ý đến token nào.

### Gợi ý tùy chỉnh
- Đổi biến `sentence` để thử câu khác.
- Thay `layer` và `head` để xem attention ở lớp hoặc head khác.
- Bỏ `annot=True` nếu muốn heatmap gọn hơn khi câu dài hơn.
