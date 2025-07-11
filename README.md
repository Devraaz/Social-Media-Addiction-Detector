# 📱 Social Media Addiction Detector

This is a machine learning-based web application that predicts a user's **social media addiction score (1–10)** and assesses whether it's **affecting their academic performance**. The application provides **personalized feedback** based on the predictions.

👉 **[Live Preview on Streamlit](https://devraaz-social-media-addiction-detector.streamlit.app/)**

---

## 📖 Overview

**Social Media Addiction Detector** uses two different machine learning models:

- 📈 **Linear Regression**: Predicts a numerical **Addiction Score** (1–10) based on user input.
- 🧠 **Logistic Regression**: Predicts whether the user's social media usage is **affecting academic performance** with a simple **Yes/No** output.

The system analyzes user inputs like age, gender, academic level, daily screen time, sleep hours, mental health score, and most-used platform to determine the results.

---

## 🧠 Models Used

| Model               | Purpose                                      |
| ------------------- | -------------------------------------------- |
| Linear Regression   | Predict social media addiction score (1–10)  |
| Logistic Regression | Predict academic performance impact (Yes/No) |

---

## 🌟 Features

- 🔢 Predicts Social Media Addiction Score (1–10)
- 📉 Determines if it affects academic performance
- 💬 Personalized message based on risk level
- 📦 Pre-trained models loaded via Pickle
- 🔒 Consistent label encoding using saved encoder
- ✅ Built with a clean and responsive **Streamlit UI**

---

## 💻 Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle

---

## 📂 File Structure

- app.py # Main Streamlit application
- sm_df.pkl # Original training DataFrame (for encoding)
- le.pkl # LabelEncoder for consistent encoding
- m1_lr.pkl # Trained Linear Regression model
- m2_lr.pkl # Trained Logistic Regression model
- README.md # Project documentation

---

## 🚀 Getting Started

### 1. Clone the repository or download the files:

```bash
git clone https://github.com/yourusername/social-media-addiction-detector.git
cd social-media-addiction-detector
```

### 2. Install dependencies:

```bash
pip install streamlit pandas scikit-learn
```

### 3. Run the application:

```bash
streamlit run app.py
```

🧾 Example Prediction
Input:

Age: 22

Gender: Female

Screen Time: 6 hrs/day

Sleep: 5 hrs/night

Mental Health Score: 4/10

Output:

Addiction Score: 8

Academic Impact: Yes

Message: "High usage detected. You may be developing an addiction. Consider reducing usage and engaging in offline activities."

🔮 Future Enhancements
Add model accuracy metrics and confidence levels

Visualizations for addiction trends

Save user history to track progress

Deploy on Hugging Face Spaces or AWS

📜 License
This project is intended for educational and research purposes only.

👨‍💻 Author
Devraj Dora

Feel free to reach out for collaboration or questions.

---

Let me know if you want the README to include a GIF preview or embed a YouTube walkthrough as well!
