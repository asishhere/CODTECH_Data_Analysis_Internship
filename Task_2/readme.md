### Intern ID: CITS414

## 🚀Getting Started

1. Clone this repository:
```
bash 

git clone [https://github.com/asishhere/CODTECH-Data-Analysis-Internship.git]
```
2. Set up local virtual environment and dependencies:
```
bash

pip install -r requirements.txt

```
---
# Task 2: Predictive Analysis Using Machine Learning — Sales Forecast

## 📝 Project Overview
This module details a supervised machine learning regression pipeline built to forecast continuous sales metrics across highly volatile conditions. The data architecture handles structural feature engineering, target encoding configurations, model optimization, and cross-model performance benchmarks.

## 🧬 Machine Learning Pipeline Structure
```text
Raw Data ➔ EDA ➔ Feature Engineering ➔ One-Hot Encoding ➔ Train/Test Split (80:20) ➔ Model Benchmarking ➔ Evaluation
```

## 🛠️ Technical Stack
Framework: Scikit-Learn
Data Layout: Pandas, NumPy
Plotting Engine: Matplotlib, Seaborn

## 🤖 Models Evaluated
1. Linear Regression: Baseline parametric architecture evaluating direct linear feature weights.
2. Random Forest Regressor: Ensemble non-parametric method utilizing decision-tree bagging to map complex multi-variant interactions.

## 📐 Evaluation Metrics
Models are verified using the following standard statistical dimensions[cite: 1]:

Mean Absolute Error (MAE): Quantifies baseline residual distance[cite: 1].
Root Mean Squared Error (RMSE): Accentuates variance and flags outlier errors[cite: 1].
Coefficient of Determination ($R^2$ Score): Evaluates overall target variance capture[cite: 1].

