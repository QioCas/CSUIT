# Restaurant Aspect-Based Sentiment Analysis (ABSA)

## Introduction

This project implements an Aspect-Based Sentiment Analysis (ABSA) system for restaurant reviews using the VLSP 2018 Restaurant dataset.

### Models and Techniques

- TF-IDF Vectorization
- Multinomial Logistic Regression (Softmax Regression)
- Grid Search Hyperparameter Tuning
- Dummy Classifier for single-label aspects

---

## Problem Definition

Each review may contain multiple aspects and sentiment labels.

### Entities

- RESTAURANT
- AMBIENCE
- LOCATION
- FOOD
- SERVICE
- DRINKS

### Attributes

- GENERAL
- PRICES
- QUALITY
- STYLE&OPTIONS
- MISCELLANEOUS

Aspect format:

```text
ENTITY#ATTRIBUTE
```

Examples:

```text
FOOD#QUALITY
SERVICE#GENERAL
AMBIENCE#GENERAL
```

---

## Dataset Format

```text
ID
Review Text
{ASPECT, POLARITY}

```

Example:

```text
1
Món ăn rất ngon nhưng phục vụ khá chậm.
{FOOD#QUALITY, positive}, {SERVICE#GENERAL, negative}
```

---

## Data Processing

1. Read raw VLSP data.
2. Extract (Aspect, Sentiment) pairs.
3. Create target vectors for each aspect.
4. Assign `null` to missing aspects.

---

## Feature Extraction

```python
TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_features=50000
)
```

---

## Model

### Logistic Regression

```python
LogisticRegression(
    solver='lbfgs',
    multi_class='multinomial',
    max_iter=500
)
```

### Hyperparameter Search

```text
C ∈ {0.01, 0.1, 1, 10, 100}
```

---

## Evaluation

Metrics:

- Accuracy
- Macro F1-score

Results are reported per aspect and averaged across all aspects.

---

## Project Structure

```text
.
├── restaurant.ipynb
├── train_data.txt
├── dev_data.txt
├── test_data.txt
└── README.md
```

---

## Installation

```bash
pip install numpy pandas scikit-learn
```

---

## Running

Open:

```text
restaurant.ipynb
```

Run all notebook cells after placing the dataset files in the same directory.

## Technologies

- Python
- Scikit-learn
- TF-IDF
- Logistic Regression
- VLSP 2018 Restaurant Dataset

---