import streamlit as st
import pickle 
import pandas as pd

# Importing Pickle File
with open('sm_df.pkl', 'rb') as file:
    sm_df = pickle.load(file)
with open('le.pkl', 'rb') as file:
    le = pickle.load(file)
with open('m1_lr.pkl', 'rb') as file:   # m1 is Linear Regression
    m1_lr = pickle.load(file)
with open('m2_lr.pkl', 'rb') as file:   # m2 is Logistic Regression
    m2_lr = pickle.load(file)


st.header("👀 Social Media Addiction Detector")
st.write("This tool analyzes your responses to predict a Social Media Addictive Score"
" (1–10) based on your usage patterns and habits. The score helps assess your risk level "
"and provides personalized feedback to guide healthier digital behavior.")
st.divider()
def encode2(user_data, original_df):
    for col in ['Gender', 'Most_Used_Platform', 'Relationship_Status', 'Academic_Level']:
        
        le.fit(original_df[col])  # Use original dataset to ensure consistency
        user_data[col] = le.transform(user_data[col])
    return user_data


def main():
    st.write("Hey Social Media Users")

    
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input("Enter Age: ", key="age_input", min_value=1, max_value=100, step=1)
        Gender = st.selectbox("Enter Gender: ", 
                            ("Male", "Female"))
        Academic_Level = st.selectbox("Enter Academic Level: ", 
                            ("Graduate", "Undergraduate", 'High School'))
    with col2:
        Avg_Daily_Usage_Hours = st.number_input("Enter Daily Screen Time (in hours): ",min_value=1, max_value=24)
        Most_Used_Platform = st.selectbox("Enter Most Used Platform: ", 
                            ("Instagram", "TikTok", "Facebook", "WhatsApp", "Twitter", "LinkedIn", "WeChat","Snapchat", "YouTube"))
        Sleep_Hours_Per_Night = st.number_input("Enter Sleep hours per night: ",min_value=1, max_value=20)

    with col3:
        Mental_Health_Score = st.number_input("Enter Mental Health Score ( out of 10): ",min_value=1, max_value=10)
        Relationship_Status = st.selectbox("Enter Relationship Status: ", 
                            ("Single", "In Relationship", "complicated"))

    
    user_data = pd.DataFrame([{
        'Age': Age,
        'Gender': Gender,
        'Academic_Level': Academic_Level,
        'Avg_Daily_Usage_Hours': Avg_Daily_Usage_Hours,
        'Most_Used_Platform': Most_Used_Platform,
        'Sleep_Hours_Per_Night': Sleep_Hours_Per_Night,
        'Mental_Health_Score': Mental_Health_Score,
        'Relationship_Status': Relationship_Status,
    }])
    if st.button("Detect", type='primary'):
        user_data = encode2(user_data, sm_df)
        st.divider()

        message = "Please check input data Properly"
        user_score = m1_lr.predict(user_data)
        user_score = int(user_score.item())
        match user_score:
            case 1 | 2:
                message = "You're doing great! Very minimal signs of social media addiction. Keep it balanced."
            case 3 | 4:
                message = "Mild usage detected. You're mostly in control, but be mindful of screen time."
            case 5 | 6:
                message = "Moderate risk. Try to evaluate your daily usage and set some limits."
            case 7 | 8:
                message = "High usage detected. You may be developing an addiction. Consider reducing usage and engaging in offline activities."
            case 9:
                message = "Severe warning. Strong signs of addiction. It's important to take action now—consider digital detox strategies."
            case 10:
                message = "Critical level of addiction. Professional help or strict interventions might be necessary to regain control."
            case _:
                message = "Invalid score. Please check input data."

        user_data_predict = m2_lr.predict(user_data)
        grade = 'No' if user_data_predict == 0 else  "Yes"


        container = st.container(border=True)

        container.write(f"Affect Academic Performance: {grade}")
        container.write(f"Your Addictive Score is: {user_score}")
        container.write(message)

main()