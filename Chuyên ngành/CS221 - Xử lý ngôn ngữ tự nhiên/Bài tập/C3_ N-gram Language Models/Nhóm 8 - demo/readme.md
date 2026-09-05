# N-gram Language Model Demo

## 1. Giới thiệu

Notebook này minh họa cách xây dựng **Language Model dựa trên N-gram** trong xử lý ngôn ngữ tự nhiên (NLP).

N-gram model ước lượng xác suất của một chuỗi từ dựa trên **(n−1) từ trước đó**.

Ví dụ:

* **Unigram:**
  (P(w))

* **Bigram:**
  (P(w_i | w_{i-1}))

* **Trigram:**
  (P(w_i | w_{i-2}, w_{i-1}))

Các mô hình này là nền tảng cho nhiều hệ thống NLP trước khi các phương pháp **neural embeddings** và **Transformer** trở nên phổ biến.

---

# 2. Dataset

Notebook sử dụng **Tiny Shakespeare corpus**.

Nguồn dữ liệu:

```
https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

Corpus này chứa toàn bộ văn bản của các vở kịch của Shakespeare và thường được sử dụng để demo các mô hình **language modeling**.

---

# 3. Nội dung Notebook

Notebook bao gồm các bước sau:

### 1. Import thư viện

Import các thư viện cần thiết như:

* `math`
* `requests`
* `collections`
* `numpy`
* `random`

---

### 2. Load corpus

Tải dữ liệu văn bản từ internet và chuẩn hóa bằng cách chuyển toàn bộ chữ sang **lowercase**.

---

### 3. Tokenize

Chuyển văn bản thành danh sách **tokens (words)** bằng cách tách theo khoảng trắng.

Ví dụ:

```
"the king is dead"
```

→

```
["the","king","is","dead"]
```

---

### 4. Build Unigram Model

Xây dựng **Unigram language model** bằng cách tính xác suất xuất hiện của từng từ:

[
P(w)=\frac{count(w)}{N}
]

Trong đó:

* (count(w)) là số lần xuất hiện của từ
* (N) là tổng số từ trong corpus

---

### 5. Build Bigram Model

Bigram model ước lượng xác suất của một từ dựa trên **từ đứng trước**.

[
P(w_i | w_{i-1}) =
\frac{count(w_{i-1},w_i)}
{count(w_{i-1})}
]

Model này học được **quan hệ ngữ cảnh đơn giản giữa các từ**.

---

### 6. Build Trigram Model

Trigram model dự đoán một từ dựa trên **hai từ trước đó**.

[
P(w_i | w_{i-2}, w_{i-1}) =
\frac{count(w_{i-2},w_{i-1},w_i)}
{count(w_{i-2},w_{i-1})}
]

So với Bigram, Trigram có thể nắm bắt **context tốt hơn**.

---

### 7. Sentence Log Probability

Tính **log probability của một câu** dựa trên Bigram model:

[
\log P(W)=\sum_{i=1}^{N}\log P(w_i|w_{i-1})
]

Việc sử dụng **log** giúp tránh hiện tượng **underflow** khi nhân nhiều xác suất nhỏ.

---

### 8. Perplexity Function

Perplexity được dùng để **đánh giá chất lượng language model**.

[
PP(W)=P(w_1,...,w_N)^{-1/N}
]

Hoặc viết dưới dạng log:

[
PP(W)=\exp\left(-\frac{1}{N}\sum_{i=1}^{N}\log P(w_i|w_{i-1})\right)
]

Perplexity càng **thấp** thì mô hình dự đoán càng **tốt**.

---

### 9. Generate Text Using Bigram

Sau khi huấn luyện Bigram model, notebook có thể **sinh văn bản mới** bằng cách:

1. chọn một từ khởi đầu
2. lấy mẫu từ phân phối xác suất (P(w_i | w_{i-1}))
3. lặp lại nhiều lần

Ví dụ kết quả:

```
the king is not so well that i ...
```

---

