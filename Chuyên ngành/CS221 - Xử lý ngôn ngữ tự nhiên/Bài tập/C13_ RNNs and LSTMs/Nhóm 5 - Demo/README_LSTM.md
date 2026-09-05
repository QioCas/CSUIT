# Vietnamese Sentiment Analysis using LSTM

## Overview

This project demonstrates how to build a Long Short-Term Memory (LSTM) neural network for Vietnamese sentiment analysis.

The notebook presents the complete deep learning pipeline, including:

- Data preparation
- Text preprocessing
- Tokenization
- Sequence padding
- LSTM model construction
- Model training and evaluation
- Sentiment prediction on new sentences

---

## Project Objective

The goal is to classify Vietnamese reviews into two sentiment categories:

| Label | Meaning |
|---------|---------|
| 1 | Positive |
| 0 | Negative |

The notebook uses a small demonstration dataset containing positive and negative customer reviews.

---

## Workflow

### 1. Data Preparation

A collection of Vietnamese review samples is created manually and labeled as:

- Positive reviews
- Negative reviews

The data is stored in a Pandas DataFrame and prepared for training.

---

### 2. Dataset Splitting

The dataset is divided into:

- Training Set
- Validation Set
- Test Set

using:

```python
train_test_split()
```

---

### 3. Text Preprocessing

The notebook applies:

#### Tokenization

```python
Tokenizer()
```

to convert words into integer indices.

#### Padding

```python
pad_sequences()
```

to ensure all sequences have the same length.

Parameters:

```python
MAX_WORDS = 5000
MAX_LEN = 20
```

---

## LSTM Architecture

The model is built using TensorFlow/Keras.

```python
Embedding(VOCAB_SIZE, 128)
LSTM(64)
Dropout(0.3)
Dense(32, activation="relu")
Dense(1, activation="sigmoid")
```

### Layer Description

#### Embedding Layer

Transforms word indices into dense vector representations.

#### LSTM Layer

Learns sequential and contextual information from text.

#### Dropout Layer

Reduces overfitting during training.

#### Dense Layers

Perform binary sentiment classification.

---

## Training

The model is trained using:

```python
optimizer="adam"
loss="binary_crossentropy"
```

Early stopping is applied to prevent overfitting:

```python
EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)
```

Training configuration:

```python
epochs = 20
batch_size = 4
```

---

## Evaluation

Performance is evaluated using:

- Accuracy
- Classification Report

```python
accuracy_score()
classification_report()
```

Metrics include:

- Precision
- Recall
- F1-score

---

## Inference

The notebook includes a custom prediction function:

```python
predict_sentiment(text)
```

Example:

```python
predict_sentiment("Sản phẩm dùng rất tốt và đáng tiền")
predict_sentiment("Dịch vụ quá tệ và tôi thất vọng")
```

Output:

- Positive sentiment probability
- Predicted label

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn

---

## Project Structure

```text
.
├── Nhóm 5_LSTM.ipynb
└── README.md
```

---

## Installation

Install required packages:

```bash
pip install tensorflow pandas numpy scikit-learn
```

---

## Running the Notebook

Open:

```text
Nhóm 5_LSTM.ipynb
```

Run all notebook cells sequentially.

The notebook will:

1. Create a sentiment dataset.
2. Tokenize and pad sequences.
3. Train an LSTM model.
4. Evaluate performance.
5. Predict sentiment for new sentences.

---

## Learning Outcomes

After completing this notebook, users will understand:

- Basic Natural Language Processing workflow.
- Text tokenization and padding.
- Word embeddings.
- Long Short-Term Memory (LSTM) networks.
- Binary sentiment classification.
- Model evaluation and inference.

---