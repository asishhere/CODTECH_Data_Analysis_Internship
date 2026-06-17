### Intern ID: CITS414

## 🚀Getting Started

1. Clone this repository:
```
bash 

git clone [https://github.com/Murli0810/CODTECH-Data-Analysis-Internship.git](https://github.com/Murli0810/CODTECH-Data-Analysis-Internship.git)

```
2. Set up local virtual environment and dependencies:
```
bash

pip install -r requirements.txt

```

# Task 4: Sentiment Analysis — Customer Feedback (NLP)

## 📝 Project Overview
This project implements a Natural Language Processing (NLP) framework designed to categorize unstructured text into distinct sentiment profiles[cite: 1]. It builds a hybrid validation engine by pairing a lexicon rule-based engine directly against a supervised text classification system[cite: 1].

## 🔀 The NLP Engineering Pipeline
```text
Text ➔ Lowercasing ➔ Punctuation Strip ➔ Tokenization ➔ Stopword Filtering ➔ Lemmatization ➔ TF-IDF Vectorization
```

## 🛠️ Technical Stack

NLP Engines: NLTK (VADER Lexicon Suite)[cite: 1]

Machine Learning: Scikit-Learn (TF-IDF Vectorizer, Logistic Regression)[cite: 1]

Visual Processing: WordCloud, Matplotlib, Seaborn[cite: 1]

## 🔬 Operational Mechanics

VADER Sentiment: Maps intent using contextual rules, tracking emojis, text capitalizations, and exclamation weights to calculate compound polarity matrices (-1 to +1)[cite: 1].

TF-IDF Vectorization: Converts preprocessed word strings into continuous numerical arrays by capturing unigram and bigram word importance[cite: 1].

Supervised Classifier: Applies a Logistic Regression classifier on top of the text arrays to accurately distinguish real sentiment trends[cite: 1].

