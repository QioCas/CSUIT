Trong bài thực hành này, chúng em xây dựng một mô hình phân loại văn bản tiếng Việt bằng Feed-Forward Neural Network sử dụng PyTorch. Yêu cầu bài toán là từ nội dung một bản tin, mô hình sẽ dự đoán bản tin đó thuộc nhóm chủ đề nào. 

Bài làm sử dụng bộ dữ liệu [`VN Topic Classification Dataset`](https://www.kaggle.com/datasets/moulsn/vn-topic-classification-dataset/).  

Tập dữ liệu có tổng cộng 4995 mẫu, mỗi mẫu gồm hai cột:
- `text`: nội dung tin tức
- `label`: nhãn chủ đề

Dữ liệu gồm 5 nhóm nhãn:
- Chính trị
- Công nghệ
- Kinh tế
- Thể thao
- văn hoá

Sau khi đọc dữ liệu ở bước tiền xử lý, chúng em xử lý các giá trị thiếu trong cột `text`, đồng thời chuẩn hóa lại khoảng trắng trong văn bản để dữ liệu gọn hơn. Cột `label` cũng được chuyển về dạng chuỗi và loại bỏ khoảng trắng thừa để tránh lỗi khi mã hóa nhãn.

Sau đó, chúng em dùng `LabelEncoder` để chuyển nhãn từ dạng chữ sang dạng số, vì mô hình học máy hoạt động tốt trên dữ liệu dạng số.

Ta sẽ chia tập dữ liệu được chia thành ba phần:
- tập train để huấn luyện mô hình
- tập dev để theo dõi kết quả trong lúc train
- tập test để đánh giá cuối cùng

Việc chia tập được thực hiện bằng `train_test_split`.

Vì mạng neural network không thể nhận trực tiếp dữ liệu văn bản thô, chúng em sử dụng `TfidfVectorizer` để biến mỗi văn bản thành một vector số. Trong notebook, TF-IDF được cấu hình với các tham số:
- `max_features=15000`
- `ngram_range=(1, 2)`
- `min_df=2`
- `max_df=0.95`
- `sublinear_tf=True`

Vectorizer được `fit` trên tập train, sau đó dùng để `transform` cho tập dev và test. Kết quả là mỗi tin tức được biểu diễn thành một vector đặc trưng có kích thước lớn, phản ánh mức độ quan trọng của các từ và cụm từ trong văn bản.

Do đầu ra của TF-IDF là ma trận sparse, chúng em viết một class dataset riêng kế thừa từ `Dataset` của PyTorch để lấy từng mẫu dữ liệu và chuyển về tensor. Rồi tạo ra `DataLoader` cho từng tập train, dev và test.

Mô hình sử dụng trong bài là một Feed-Forward Neural Network có kiến trúc:


Trong phần huấn luyện, chúng em sử dụng:
- hàm mất mát `CrossEntropyLoss`
- bộ tối ưu `AdamW`
- learning rate `1e-3`
- weight decay `1e-4`

Ngoài ra, chúng em viết hàm `run_epoch()` để gom chung phần train và đánh giá. Ở mỗi epoch, chương trình sẽ tính loss, accuracy và macro F1-score trên tập train và tập dev.

Để tránh train quá lâu hoặc bị overfitting, chúng em có xài early stop.

Sau khi huấn luyện xong, chúng em nạp lại trọng số tốt nhất rồi đánh giá trên tập test. Kết quả thu được là:
- Test loss: `0.0677`
- Test accuracy: `0.9760`
- Test macro F1-score: `0.9759`
