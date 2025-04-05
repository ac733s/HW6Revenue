
# 🎬 Movie Revenue Estimation Using Linear Regression

This project explores the use of **multiple linear regression** to predict box office revenue based on key features such as production budget, genre popularity, and cast star power. The model is built using **Python** and **scikit-learn**, and the analysis is explained in detail through a LaTeX-based academic report.

---

## 📁 Project Contents

| File Name              | Description |
|------------------------|-------------|
| `BoxOfficeSuccess.py`      | Python script for reading data, training the model, and making predictions |
| `HW 6 Data.xlsx`       | Dataset used for training and testing the regression model |
| `HW6_Report.pdf`       | Final academic report containing model explanation and results |
| `Colab_Link.txt`       | Google Colab notebook link in plain text format |

---

## 🚀 Objective

To train a **multiple linear regression model** that predicts how much revenue a movie might earn at the box office, based on:
- 🎬 **Production Budget**
- 🔥 **Genre Popularity**
- 🌟 **Cast Star Power**

---

## 🧠 Model Summary

The regression model uses the following form:

```
Revenue = Intercept + (Weight1 × Budget) + (Weight2 × Genre) + (Weight3 × Cast)
```

**Trained Coefficients:**
- Intercept: `-103.86`
- Budget Weight: `3.60`
- Genre Weight: `9.80`
- Cast Weight: `13.56`

---

## 💡 Sample Prediction

**Input Values:**
- Production Budget = 120
- Genre Popularity = 8
- Cast Star Power = 6

**Predicted Revenue:**
```
= -103.86 + (3.60 × 120) + (9.80 × 8) + (13.56 × 6)
= 487.90 million USD (approx.)
```

---

## 📊 Visual Output

A visual screenshot of the prediction result is included in the report as a figure.

---

## 🔗 Submission Links

- ▶️ **Colab Notebook:**  
  [Google Colab](https://colab.research.google.com/drive/1LRnPvhHdYwXlXGBUZTg90_Cegz00j_v6)

- 🗃️ **GitHub Repository:**  
  [View on GitHub](https://github.com/ac733s/HW6Revenue)

---

## 👨‍🎓 Author Info

**Student:** Charan  
**Date:** April 5, 2025

---

## ✅ How to Run the Code

1. Ensure `HW 6 Data.xlsx` is in the same directory as `MovieRevenue.py`.
2. Run the script using any Python 3 environment:

```bash
python MovieRevenue.py
```

---

## ✍️ Report Details

- Format: Written in LaTeX
- Includes: Step-by-step explanation, coefficients, prediction logic, visual output, and submission links.
