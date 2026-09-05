# Aspect-Based Sentiment Analysis với Softmax Regression

Dự án này chứa Jupyter Notebook triển khai mô hình phân loại **Multinomial Logistic Regression** phục vụ cho bài toán Khai phá ý kiến trên tập dữ liệu **đánh giá khách sạn (Hotel)** của cuộc thi **VLSP 2018**:

Các Notebook đều bao gồm các bước:
1. Đọc và tiền xử lý dữ liệu.
2. Tự động sinh danh sách các Aspect có thể xảy ra từ việc kết hợp **Entity** và **Attribute**.
3. Trích xuất đặc trưng văn bản bằng thuật toán **TF-IDF**.
4. Huấn luyện mô hình
6. Tính toán điểm đánh giá mô hình bằng 2 độ đo trung bình là **Accuracy** và **Macro F1-Score**.

## 1. Yêu cầu cài đặt (Dependencies)

Các Notebook được viết bằng Python 3 và yêu cầu các thư viện học máy thông dụng. Nếu sử dụng mô trường ảo (như Conda, Virtualenv) thì có thể kích hoạt môi trường của mình, sau đó cài đặt trực tiếp qua `pip` hoặc `conda`.

Các thư viện cần thiết:
- re
- scikit-learn
- random

## 2. Hướng dẫn sử dụng
### Chọn cách chạy

#### Cách 1: Chạy bằng Jupyter Notebook (Môi trường Web)
1. Mở terminal và trỏ đến thư mục chứa bài code này.
2. Gõ lệnh:
   ```bash
   jupyter notebook
   ```
3. Một giao diện web tại `localhost:8888` sẽ mở lên, bạn click chuột trực tiếp để mở các file `.ipynb` tương ứng.
4. Bấm `Run` -> `Run All Cells` trên thanh menu để hệ thống lần lượt chạy từ file đọc dữ liệu đến in ra kết quả cuối cùng.

#### Cách 2: Chạy bằng Visual Studio Code (VS Code) / Pycharm
1. Đảm bảo VS Code đã cài đặt extension **Jupyter**.
2. Mở dự án trong VS Code. Double click để mở 1 trong 2 file `ipynb`.
3. Phía góc phải trên cùng màn hình file mã, **Select Kernel** và chọn đúng môi trường ảo Python bạn đã thực thi cài đặt thư viện ở *bước 1*.
4. Bấm nút **Run All** ở thanh công cụ của số Notebook và chờ kết quả in xuất ra ở các cell cuối của file.

#### Cách 3: Đẩy thẳng lên Google Colab
1. Truy cập [Google Colab](https://colab.research.google.com).
2. Tải 2 file `.ipynb` cùng với folder dữ liệu nhãn `.txt` (`VLSP2018-SA-train-dev-test`) lên môi trường Colab.
3. Việc cài đặt thư viện `scikit-learn`, `re` là không cần thiết vì Colab đã hỗ trợ mặc định đầy đủ. Bạn chỉ việc chạy thẳng và lấy kết quả. 

---