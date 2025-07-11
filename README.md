# 📱 Social Media Addiction Detector

This is a machine learning-based web application built using **Streamlit** that predicts a user's level of **social media addiction (1–10)** and assesses whether it might be affecting their **academic performance**. The app also provides personalized feedback and recommendations.

---

## 🔍 What it Does

- 🧠 Predicts **Addiction Score** (1–10) using a trained **Linear Regression** model
- 🎓 Predicts whether the user's social media use is **affecting academic performance** using a **Logistic Regression** model
- 📊 Gives customized advice based on the predicted score
- 📦 Uses previously trained models and label encoders saved via **Pickle**

---

## 📂 File Structure

```bash
├── app.py               # Main Streamlit application
├── sm_df.pkl            # Original training DataFrame (for consistent encoding)
├── le.pkl               # LabelEncoder for categorical features
├── m1_lr.pkl            # Trained Linear Regression model
├── m2_lr.pkl            # Trained Logistic Regression model
├── README.md            # Project documentation (this file)



```
