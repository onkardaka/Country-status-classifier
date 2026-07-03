# MODEL 2: Country Development Status Classifier

Welcome! This is **MODEL 2** in my Artificial Intelligence portfolio. In this project, I have trained a **Machine Learning** algorithm capable of classifying whether a country is considered "Developed" or "Developing" based on its socio-economic indicators.

**[CLICK HERE TO TRY THE LIVE APP](https://country-status-classifier.streamlit.app)**

---

## 📊 Project Features

* **Algorithm Used:** Logistic Regression (Binary Classification).
* **Model Accuracy:** **90.1%** achieved on the test dataset.
* **Predictor Variables Used:**
  1. `Schooling` (Average years of schooling).
  2. `Income composition of resources` (Human Development Index efficiency score).

## 🛠️ Tools & Libraries Used
* **Python** for core development.
* **Pandas** for data cleaning and preprocessing (including handling missing values with `.dropna()` and removing hidden whitespace with `.str.strip()`).
* **Scikit-Learn** for data splitting (`train_test_split`), model training, and metrics evaluation.
* **Joblib** for freezing and exporting the trained model's "brain".
* **Streamlit Cloud** for deploying the live interactive web interface into production.

---
*This project is part of my specialized Machine Learning roadmap, advancing from linear models toward classification algorithms and production deployment.*
