# Masked Language Models (BERT) Demo

## Overview

This project demonstrates the core concepts of **Masked Language Models (MLM)** using BERT and provides practical examples with the Hugging Face Transformers ecosystem.

The notebook focuses on:

1. Understanding Masked Language Models.
2. Exploring Contextual Embeddings.
3. Analyzing Word Sense through context.
4. Fine-tuning BERT for Sequence Classification.
5. Sentiment Analysis on the IMDB Movie Reviews dataset.

---

## Objectives

### Part 1: Contextual Embeddings

This section demonstrates how BERT generates different vector representations for the same word depending on its surrounding context.

Example:

- "mouse" as an animal.
- "mouse" as a computer device.

The notebook extracts contextual embeddings from BERT and compares semantic similarities using cosine similarity.

---

### Part 2: Fine-Tuning BERT

This section fine-tunes a pre-trained BERT model for binary sentiment classification.

Task:

- Positive Review
- Negative Review

Dataset:

- IMDB Movie Reviews

A smaller subset of the dataset is used to reduce training time during demonstration.

---

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Evaluate
- Scikit-learn
- BERT Base Uncased

---

## Model Architecture

### Contextual Embedding Model

```python
BertModel.from_pretrained("bert-base-uncased")
```

Used for:

- Extracting hidden states
- Generating contextual word embeddings
- Measuring semantic similarity

### Sequence Classification Model

```python
AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)
```

Used for:

- Binary sentiment classification
- Fine-tuning on IMDB reviews

---

## Dataset

### IMDB Movie Reviews

The notebook loads the dataset directly from Hugging Face:

```python
load_dataset("imdb")
```

Classes:

- 0: Negative
- 1: Positive

Demo subset:

- 1000 training samples
- 200 testing samples

---

## Evaluation

The notebook evaluates the classification model using:

- Accuracy

via:

```python
evaluate.load("accuracy")
```

---

## Example Predictions

After fine-tuning, the model is tested on custom movie reviews such as:

```text
This movie was absolutely fantastic!
```

```text
What a waste of time.
```

```text
It was okay, not the best but I had a good time watching it.
```

The model predicts the corresponding sentiment label.

---

## Installation

Install required libraries:

```bash
pip install transformers datasets evaluate torch scikit-learn
```

---

## Running the Notebook

Open:

```text
Nhóm 5 _ Masked_Language_Models.ipynb
```

Run all cells sequentially.

The notebook will:

1. Load pre-trained BERT.
2. Demonstrate contextual embeddings.
3. Load the IMDB dataset.
4. Fine-tune BERT for sentiment classification.
5. Evaluate and test predictions.

---

## Learning Outcomes

After completing this notebook, users will understand:

- How Masked Language Models work.
- Why contextual embeddings outperform static embeddings.
- How BERT represents word meaning in different contexts.
- The workflow of fine-tuning transformer models.
- Practical sentiment analysis using BERT.

---