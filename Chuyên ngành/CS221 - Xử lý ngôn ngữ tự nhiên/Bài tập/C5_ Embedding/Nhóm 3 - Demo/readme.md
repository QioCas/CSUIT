# Word Embeddings Demo using Word2Vec

## 1. Giới thiệu

Demo này minh họa cách sử dụng **Word Embeddings** trong NLP bằng mô hình **Word2Vec**.

Theo *Chapter 5 – Embeddings*, ý tưởng chính của embeddings là:

> Words that appear in similar contexts tend to have similar meanings.

Mỗi từ được biểu diễn bằng một **vector số trong không gian nhiều chiều**.
Các vector gần nhau trong không gian này thường có **ý nghĩa ngữ nghĩa giống nhau**.

Ví dụ:

```
king − man + woman ≈ queen
```

Demo này sử dụng **pretrained Word2Vec model từ Google News** và thư viện **Gensim**.

---

# 2. Dataset

Dataset Word2Vec pretrained:

Download tại đây:

[Download dataset](https://drive.google.com/drive/folders/1_uDleDZ0CwdKV77lg4gw83rQQVn6a8eN)

Dataset gốc:

```
GoogleNews-vectors-negative300.bin
```

File này chứa:

* ~3 triệu từ
* vector dimension = 300
* được huấn luyện trên **Google News corpus**

Do file rất lớn (~3.6GB), demo này sử dụng phiên bản rút gọn.

---

# 3. Cài đặt môi trường

Cài đặt thư viện cần thiết:

```bash
pip install gensim
pip install gdown
```

---

# 4. Chuẩn bị model Word2Vec

Vì model gốc rất lớn, bước đầu tiên là **rút gọn vocabulary** để phù hợp với bộ nhớ máy.

```python
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    "GoogleNews-500k.bin",
    binary=True,
    limit=50000
)

model.save_word2vec_format(
    "GoogleNews-50k.bin",
    binary=True
)
```

Ý nghĩa:

* `load_word2vec_format()`
  load pretrained Word2Vec model

* `limit=50000`
  chỉ giữ **50k từ phổ biến nhất**

Kết quả:

```
GoogleNews-50k.bin
```

---

# 5. Load model và lấy embedding vector

## Mục tiêu

Lấy vector embedding của một từ.

Theo chương 5:

> Mỗi từ được biểu diễn bằng một vector trong không gian nhiều chiều.

### Code

```python
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    'GoogleNews-50k.bin',
    binary=True,
    limit=500000
)

word = input('input your word to show embedding vector: ')

if word in model:
    embedding = model[word]
    print("Vector của từ:", embedding[:10])
else:
    print("Từ này không có trong từ điển!")
```

### Ví dụ

Input:

```
king
```

Output:

```
[0.125, -0.098, 0.043 ...]
```

Vector này có **300 chiều**.

---

# 6. Word Analogy (Vector Arithmetic)

Theo chương 5:

Embeddings có thể biểu diễn **quan hệ ngữ nghĩa**.

Ví dụ:

```
king − man + woman = queen
```

### Code

```python
result = model.most_similar(
    positive=['Messi','Female'],
    negative=['Male'],
    topn=3
)

for word, similarity in result:
    print(word, similarity)
```

### Ý nghĩa

Tính:

```
Messi - Male + Female
```

→ tìm từ có vector gần nhất.

---

## 6.1 Trường hợp tổng quát

Cho phép nhập nhiều từ.

```python
pos = list(input().split())
neg = list(input().split())

result = model.most_similar(
    positive=pos,
    negative=neg,
    topn=3
)

for word, score in result:
    print(word, score)
```

Ví dụ:

```
positive: king woman
negative: man
```

Kết quả:

```
queen
```

---

# 7. Tìm từ đồng nghĩa (Similar Words)

Mục tiêu:

Tìm các từ **có embedding gần nhau**.

### Code

```python
w1 = input("input your word: ")

result = model.most_similar(w1, topn=3)

for word, score in result:
    print(word, score)
```

Ví dụ:

Input:

```
car
```

Output:

```
vehicle
automobile
truck
```

Điều này xảy ra vì:

```
cosine similarity(vector_car, vector_vehicle) ≈ 1
```

---

# 8. Đo độ tương đồng giữa hai từ

Theo chương 5, similarity được đo bằng **cosine similarity**.

Công thức:

```
cos(v,w) = (v·w) / (|v||w|)
```

### Code

```python
w1, w2 = input().split()

print(model.similarity(w1, w2))
```

Ví dụ:

```
king queen
```

Output:

```
0.72
```

---

# 9. Tìm từ khác loại

Bài toán:

Trong một tập từ, tìm từ **không cùng nhóm**.

### Code

```python
w = ['apple','orange','lemon','sport','watermelon']

uni_word = model.doesnt_match(w)

print(uni_word)
```

Output:

```
sport
```

Vì các từ còn lại đều là **fruit**.

---

# 10. Mini Game: Dự đoán thủ đô

Sử dụng **analogy relation**:

```
Iran : Tehran
France : Paris
```

### Code

```python
def predict_capital(country):
    result = model.most_similar(
        positive=['Tehran', country],
        negative=['Iran'],
        topn=1
    )

    return result[0][0], result[0][1]
```

### Ví dụ

Input:

```
France
```

Output:

```
Paris
```

---

# 11. Evaluation Model

Test model bằng tập dữ liệu country-capital.

```python
correct = 0

for country, capital in country_capital_test.items():
    ans,_ = predict_capital(country)

    if ans == capital:
        correct += 1

print('Accuracy:', correct/len(country_capital_test))
```

Accuracy cho biết:

```
embedding có học được quan hệ country-capital hay không
```

---

# 12. Kết luận

Demo này minh họa các khả năng của **word embeddings**:

1. biểu diễn từ bằng vector
2. tìm từ giống nghĩa
3. tính similarity
4. giải bài toán analogy
5. suy luận quan hệ ngữ nghĩa

Những tính chất này được mô tả trong **Chapter 5 – Embeddings** của sách:

```
Speech and Language Processing
Jurafsky & Martin
```

Embeddings là nền tảng cho nhiều hệ thống NLP hiện đại như:

* Machine Translation
* Question Answering
* Chatbot
* Large Language Models
