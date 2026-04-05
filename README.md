# Network Traffic Analysis using Machine Learning

> Machine Learning based Network Traffic Attack Detection System

---

## 📌 Project Overview
This project focuses on detecting malicious network traffic using Machine Learning techniques.  
The UNSW-NB15 dataset is used to classify network packets as **normal (0)** or **attack (1)**.

---

## ⚙️ Tools & Technologies
- Python  
- Pandas  
- NumPy  
- Scikit-learn (Random Forest)  

---

## 📊 Dataset
- Dataset used: **UNSW-NB15**  
- Contains network traffic features such as IP addresses, ports, protocols, and packet-level information  

---

## 🔄 Project Workflow

1. Load dataset  
2. Data cleaning & preprocessing  
   - Removed IP-related columns  
   - Converted all values to numeric  
   - Handled missing values  
3. Feature & target split  
4. Train-test split (80-20)  
5. Model training using **Random Forest Classifier**  
6. Prediction and evaluation  

---

## 📈 Results

- **Accuracy:** ~99%  
- **ROC-AUC Score:** ~0.99  

---

## 📊 Evaluation Metrics

- Confusion Matrix  
- Classification Report  
  - Precision  
  - Recall  
  - F1-score  

---

## 🔍 Feature Importance

Top important features influencing predictions were identified using:
- `model.feature_importances_`

---

## 🚀 Future Improvements

- Integration with **Apache Spark / Hadoop** for big data processing  
- Real-time traffic monitoring system  
- Advanced anomaly detection models  

---

## 📂 Files in Repository

- `main.py` → Main project code  
- `README.md` → Project documentation  

---

## 👨‍💻 Author

Gnyaaneshwar
