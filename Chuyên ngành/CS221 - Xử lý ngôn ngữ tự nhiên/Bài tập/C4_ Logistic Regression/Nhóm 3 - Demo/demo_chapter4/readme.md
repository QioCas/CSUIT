# Phân loại cảm xúc văn bản bằng Logistic Regression

## 1. Giới thiệu

Project này cài đặt một hệ thống **phân loại văn bản (text classification)** sử dụng **Logistic Regression** dựa trên nội dung trong sách *Speech and Language Processing* của Daniel Jurafsky và James H. Martin.

Mục tiêu của notebook là xây dựng một mô hình **phân tích cảm xúc (sentiment analysis)** để phân loại câu văn thành ba nhãn:

- Negative (tiêu cực)
- Neutral (trung lập)
- Positive (tích cực)

Trong xử lý ngôn ngữ tự nhiên (NLP), **phân loại văn bản** là nhiệm vụ gán một nhãn cho một văn bản đầu vào.

Logistic Regression là một **bộ phân loại xác suất**. Mô hình tính:

$$z = w \times x + b$$

Trong đó:

- x : vector đặc trưng (feature vector)
- w : vector trọng số (weight vector)
- b : bias

Giá trị z được đưa qua **hàm sigmoid** để biến đổi thành xác suất từ 0 đến 1. :contentReference[oaicite:0]{index=0}

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Nếu xác suất lớn hơn **0.5**, mô hình dự đoán lớp 1; nếu nhỏ hơn thì dự đoán lớp 0.

Trong notebook này, Logistic Regression được mở rộng thành **multiclass classification** để phân loại ba nhãn cảm xúc.

---

# 2. Cài đặt môi trường

## Phiên bản Python

Khuyến nghị:

Python 3.8+

## Các thư viện cần cài đặt

Cài đặt bằng pip:

pip install numpy pandas scikit-learn

### Các thư viện chính

| Thư viện | Mục đích |
|--------|--------|
| pandas | xử lý dữ liệu |
| glob | đọc nhiều file |
| os | xử lý đường dẫn |
| re | xử lý văn bản |
| scikit-learn | thư viện machine learning |
| TfidfVectorizer | chuyển văn bản thành vector |
| LogisticRegression | mô hình phân loại |

---

# 3. Cấu trúc dữ liệu

Notebook đọc dữ liệu từ thư mục:

VLSP2018-SA-train-dev-test/

Ví dụ cấu trúc:

VLSP2018-SA-train-dev-test/
    train.txt
    dev.txt
    test.txt

Mỗi dòng dữ liệu có dạng:

Ví dụ:

2   Phim này rất hay

0   Nội dung quá tệ

1   Phim bình thường

Ý nghĩa của label:

| Label | Ý nghĩa |
|------|------|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

---

# 4. Các bước implement

Notebook được chia thành các bước chính sau.

---

# Bước 1 — Import thư viện

Code:

```python
import pandas as pd
import glob
import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
```

Mục đích:

* Import các thư viện cần thiết
* Sử dụng công cụ machine learning từ **scikit-learn**


# Bước 2 — Đọc dữ liệu

Code:

```python
path = './VLSP2018-SA-train-dev-test'
all_files = glob.glob(os.path.join(path, "*.txt"))

texts, labels = [], []

for filename in all_files:
    with open(filename, 'r', encoding='utf-8-sig') as f:
        ...
```

Mục đích:

1. Đọc tất cả file `.txt`
2. Tách:

   * văn bản
   * nhãn

Kết quả:

texts = ["sentence1", "sentence2", ...]

labels = [0,1,2,...]

---

# Bước 3 — Chuyển văn bản thành vector

Code:

```python
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    token_pattern=r'(?u)\b\w\w+\b'
)

X = vectorizer.fit_transform(texts)
y = labels
```

Mục đích:

Máy học **không xử lý trực tiếp văn bản**, nên cần chuyển thành **vector số**.

Phương pháp sử dụng:

**TF-IDF (Term Frequency – Inverse Document Frequency)**

Ý nghĩa:

* đo mức độ quan trọng của từ trong văn bản.

Các tham số:

| Tham số           | Ý nghĩa                   |
| ----------------- | ------------------------- |
| ngram_range=(1,2) | sử dụng unigram và bigram |
| token_pattern     | quy tắc nhận dạng từ      |

Kết quả:

X $\to$ ma trận TF-IDF

y $\to$ vector nhãn

---

# Bước 4 — Huấn luyện Logistic Regression

Code:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(
    multi_class='multinomial',
    solver='lbfgs',
    max_iter=1000
)

model.fit(X_train, y_train)
```

Giải thích:

### Chia dữ liệu

80% train
20% test

### Cấu hình mô hình

| Tham số                   | Ý nghĩa                    |
| ------------------------- | -------------------------- |
| multi_class='multinomial' | logistic regression đa lớp |
| solver='lbfgs'            | thuật toán tối ưu          |
| max_iter                  | số vòng lặp                |

Quy trình huấn luyện:

1. khởi tạo trọng số
2. tính xác suất dự đoán
3. tính hàm loss
4. cập nhật trọng số
5. lặp lại

---

# Bước 5 — Đánh giá mô hình

Code:

```python
print("Độ chính xác chi tiết:")

print(
classification_report(
y_test,
model.predict(X_test),
target_names=['Neg','Neu','Pos']
))

print(confusion_matrix(y_test, y_pred))
```

Các chỉ số đánh giá:

| Metric    | Ý nghĩa                            |
| --------- | ---------------------------------- |
| Precision | độ chính xác                       |
| Recall    | khả năng tìm đúng                  |
| F1-score  | trung bình của precision và recall |

Ví dụ output:

precision recall f1-score support

Neg
Neu
Pos

---

# Confusion Matrix

Confusion matrix cho biết:

* dự đoán đúng
* dự đoán sai

Ví dụ:

```
        Pred
        N  U  P
True N 10  2  1
True U  1  8  2
True P  0  3 12
```

---

# Bước 6 — Hàm dự đoán

Code:

```python
def my_prediction(new_sentence):

    vector_cau_moi = vectorizer.transform([new_sentence])

    y_pred = model.predict(vector_cau_moi)

    return y_pred
```

Quy trình:

1. chuyển câu thành TF-IDF vector
2. đưa vào model
3. trả về nhãn

Ví dụ:

```
my_prediction("Phim này rất hay")
$\to$ Positive
```

---

# 7. Cách chạy notebook

### Bước 1

Cài thư viện (thường có sẵn):

```
pip install numpy pandas scikit-learn
```

### Bước 2

Chuẩn bị dataset:

```
VLSP2018-SA-train-dev-test/
```

### Bước 3

Chạy Jupyter:

```
jupyter notebook
```

### Bước 4

Chạy lần lượt các cell:

1 Import thư viện
2 Load dữ liệu
3 TF-IDF
4 Train model
5 Evaluate
6 Predict

---

# 8. Giải thích kết quả

Mô hình tốt khi:

* F1-score cao
* Precision và Recall cân bằng
* Confusion matrix có nhiều giá trị trên đường chéo

Các vấn đề thường gặp:

| Vấn đề         | Nguyên nhân            |
| -------------- | ---------------------- |
| Recall thấp    | bỏ sót nhiều dữ liệu   |
| Precision thấp | dự đoán sai nhiều      |
| Lệch lớp       | dataset không cân bằng |

---

# 9. Mở rộng

Một số cải tiến có thể thực hiện.

### Cải tiến feature

* loại bỏ stopwords
* stemming
* word embedding

### Cải tiến model

* SVM
* Naive Bayes
* Neural Network
* BERT

### Cải tiến dữ liệu

* tăng dữ liệu
* data augmentation

---

# 10. Tài liệu tham khảo

1. Jurafsky & Martin
   Speech and Language Processing

2. Scikit-learn documentation

3. VLSP Sentiment Analysis Dataset
