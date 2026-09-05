# Vietnamese ABSA using BiLSTM

Notebook này triển khai bài toán **Gán nhãn ngữ liệu aspect-sentiment cho chủ đề Khách Sạn (Hotel)** cho tiếng Việt theo hướng **multi-label classification**. Mỗi câu có thể mang nhiều nhãn aspect-sentiment cùng lúc, ví dụ `room_positive`, `service_negative`.

Luồng xử lý của notebook gồm:
1. Đọc dữ liệu train/dev/test theo định dạng VLSP.
2. Tách cặp `(aspect, sentiment)` từ dòng nhãn.
3. Tạo vocabulary từ tập train.
4. Mã hoá câu thành chuỗi id có độ dài cố định.
5. Mã hoá nhãn đa nhãn bằng `MultiLabelBinarizer`.
6. Tạo `Dataset` và `DataLoader`.
7. Huấn luyện mô hình `BiLSTM`.
8. Đánh giá bằng `micro F1` và `macro F1`.
9. Dự đoán thử trên một câu mẫu.

## 1. Yêu cầu cài đặt

Notebook dùng Python 3 và các thư viện chính sau:
- `torch`
- `numpy`
- `scikit-learn`

Dữ liệu cần đặt cùng thư mục với notebook, gồm:
- `1-VLSP2018-SA-Hotel-train (7-3-2018).txt`
- `2-VLSP2018-SA-Hotel-dev (7-3-2018).txt`
- `3-VLSP2018-SA-Hotel-test (8-3-2018).txt`

## 2. Hướng dẫn sử dụng

### Chuẩn bị
1. Đặt các file dữ liệu vào cùng thư mục với notebook.
2. Mở notebook và chạy lần lượt các cell từ trên xuống dưới.

### Chạy trên Jupyter Notebook
1. Mở terminal tại thư mục chứa notebook.
2. Chạy `jupyter notebook`.
3. Mở file notebook và chọn Run All Cells.

### Chạy trên VS Code
1. Cài extension Jupyter.
2. Mở notebook bằng VS Code.
3. Chọn đúng kernel Python.
4. Chạy toàn bộ notebook.

### Chạy trên Google Colab
1. Upload notebook lên Colab.
2. Upload các file `.txt` dữ liệu lên session.
3. Chạy toàn bộ notebook từ trên xuống dưới.

## 3. Giải thích các phần chính

### 3.1. Nạp dữ liệu
Notebook đọc từng dòng dữ liệu, nhận diện câu và các nhãn đi kèm. Mỗi nhãn được ghép thành chuỗi dạng `aspect_sentiment` để dùng cho bài toán phân loại đa nhãn.

### 3.2. Tiền xử lý và tạo từ điển
Câu được chuyển sang chữ thường và tách bằng khoảng trắng. Sau đó notebook đếm tần suất từ trong tập train để xây dựng vocabulary, thêm hai token đặc biệt là `<pad>` và `<unk>`.

### 3.3. Mã hoá nhãn
`MultiLabelBinarizer` biến danh sách nhãn của mỗi câu thành vector 0/1. Đây là cách chuẩn cho bài toán mà một câu có thể thuộc nhiều lớp cùng lúc.

### 3.4. Dataset và DataLoader
`ABSADataset` trả về cặp `(x, y)` cho từng mẫu, trong đó `x` là chuỗi token id và `y` là vector nhãn. `DataLoader` gom dữ liệu thành batch để train hiệu quả hơn.

### 3.5. Mô hình BiLSTM
Mô hình gồm:
- lớp `Embedding` để học biểu diễn từ,
- lớp `BiLSTM` để nắm ngữ cảnh hai chiều,
- lớp `Linear` để dự đoán xác suất cho từng nhãn.

Kết quả từ LSTM được lấy trung bình theo chiều thời gian trước khi đưa qua lớp phân loại cuối cùng.

### 3.6. Huấn luyện và đánh giá
Mô hình dùng `BCEWithLogitsLoss` vì đây là bài toán multi-label. Trong đánh giá, notebook dùng `sigmoid` để đổi logits thành xác suất rồi áp ngưỡng 0.5 để quyết định nhãn nào được chọn. Chỉ số chính là `micro F1` và `macro F1`.

### 3.7. Dự đoán thử
Sau khi train xong, notebook thử dự đoán trên câu `"Khách sạn gần biển, giá rẻ"` để kiểm tra mô hình sinh ra các nhãn nào.

## 4. Ghi chú
- Đây là baseline đơn giản, chưa dùng tokenizer tiếng Việt chuyên biệt.
- Nếu muốn cải thiện, có thể thay BiLSTM bằng transformer, thêm attention, hoặc dùng word embedding tốt hơn.
