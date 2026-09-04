import streamlit as st
import pandas as pd
import joblib



# Page Configuration

st.set_page_config(
    page_title="Student Mental Health Prediction",
    page_icon="🧠",
    layout="centered"
)


# Load Trained Model

MODEL_PATH = "best_model.pkl"

model = joblib.load(MODEL_PATH)


# Title

st.title("🧠 Student Mental Health Score Prediction")

st.write(
    "Enter the student's information below to predict "
    "the Mental Health Score."
)



# Input Section

st.subheader("Student Information")

Age = st.slider("Age", 18, 100, 20)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

Country = st.text_input(
    "Country",
    value="India"
)

Academic_Level = st.selectbox(
    "Academic Level",
    ["High School", "Undergraduate", "Graduate"]
)

Most_Used_Platform = st.selectbox(
    "Most Used Platform",
    ['Instagram',
    'TikTok',
    'Facebook',
    'LinkedIn',
    'YouTube',
    'Twitter',
    'Snapchat',
    'WhatsApp',
    'LINE',
    'VKontakte',
    'KakaoTalk',
    'WeChat']
)

Purpose_Of_Use = st.selectbox(
    "Purpose Of Use",
    ['Entertainment', 'Education', 'Networking', 'News']
)

Avg_Daily_Usage_Hours = st.number_input(
    "Average Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.1
)

Daily_Unlocks = st.number_input(
    "Daily Unlocks",
    min_value=0,
    max_value=500,
    value=50,
    step=1
)

Study_Hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.1
)

Physical_Activity_Hours = st.number_input(
    "Physical Activity Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0,
    step=0.1
)

Sleep_Hours_Per_Night = st.number_input(
    "Sleep Hours Per Night",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.1
)

Stress_Level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High", "Very High"]
)

Grouped_country = st.text_input(
    "Grouped Country",
    value="India"
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Mental Health Score"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Age": [Age],
        "Gender": [Gender],
        "Country": [Country],
        "Academic_Level": [Academic_Level],
        "Most_Used_Platform": [Most_Used_Platform],
        "Purpose_Of_Use": [Purpose_Of_Use],
        "Avg_Daily_Usage_Hours": [Avg_Daily_Usage_Hours],
        "Daily_Unlocks": [Daily_Unlocks],
        "Study_Hours": [Study_Hours],
        "Physical_Activity_Hours": [Physical_Activity_Hours],
        "Sleep_Hours_Per_Night": [Sleep_Hours_Per_Night],
        "Stress_Level": [Stress_Level],
        "Grouped_country": [Grouped_country]
    })


    # Prediction
    prediction = model.predict(input_data)[0]


    # Display result
    st.success(
        f"Predicted Mental Health Score: {prediction:.2f}"
    )
