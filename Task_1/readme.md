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

# Task 1: Big Data Analysis — Personal Expense Analytics

## 📝 Project Overview
This project targets computational constraints associated with loading high-volume datasets into standard system RAM. Utilizing **Dask**, the pipeline reads, partitions, and aggregates a synthetically scaled personal finance data framework containing 500,000 transaction matrices to surface spending anomalies and categorical distributions.

## ⚙️ Core Architecture & Concepts
*   **Lazy Evaluation:** Operations optimize memory layout by construction of a task graph, postponing resource execution until `.compute()` is distinctly invoked.
*   **Data Partitioning:** Large-scale CSV arrays are segmented into distinct algorithmic chunks allowing multi-core CPU parallelization.

## 🛠️ Technical Stack
*   **Engine:** Dask DataFrame Engine
*   **Analytics Processing:** Pandas, NumPy
*   **Visual Artifacts:** Matplotlib, Seaborn

## 📊 Key Analytical Dimensions
1. **Categorical Spend Volume:** Pinpoints baseline transactional weight across distinct consumption sectors.
2. **Temporal Trends:** Monthly transactional line vectors mapped across a multi-year horizon.
3. **Payment Modality Share:** Percentile distributions of digital vs. fiat asset routing.
4. **Day-of-Week Activity:** Mean expenditures isolated across weekly cycles.
5. **User Demographics:** Outlier threshold mapping identifying high-volume users.

