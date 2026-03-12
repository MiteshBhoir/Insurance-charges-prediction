import streamlit as st
import pandas as pd
import joblib

# Load your model and expected columns
model = joblib.load('LinearRegression.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.set_page_config(page_title="Insurance Prediction", page_icon="💰", layout="centered")
st.title("💰 Insurance Prediction by Mitesh ")
st.markdown("Provide the following details for a personalized prediction:")

# User inputs
age = st.slider("Age", 18, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Number of Children", 0, 10, 0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Southwest", "Other"])  

# Automatically determine BMI category
bmi_category_obese = 1 if bmi >= 30 else 0

if st.button("Predict"):
    # Prepare input dictionary
    raw_input = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "is_female": 1 if gender == "Female" else 0,
        "is_smoker": 1 if smoker == "Yes" else 0,
        "region_southwest": 1 if region == "Southwest" else 0,
        "bmi_category_Obese": bmi_category_obese
    }

    input_df = pd.DataFrame([raw_input])

    # Ensure all expected columns exist
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]

    # Scale only numerical columns
    numerical_cols = ['age', 'bmi', 'children']
    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

    # Predict
    prediction = model.predict(input_df)[0]
    prediction_rounded = round(prediction, 2)
    formatted_prediction = f"${prediction_rounded:,.2f}"

    # Display result with interactive style
    st.markdown("---")
    st.subheader("Your Predicted Insurance Cost:")
    st.success(f"💵 {formatted_prediction}")

    # Warnings for risk factors
    if smoker == "Yes":
        st.warning("⚠️ Smoking increases insurance cost!")
    if bmi_category_obese:
        st.warning("⚠️ High BMI (Obese) may increase insurance cost!")

    # Visual representation
    st.progress(min(prediction / 50000, 1.0))  # assumes 50k is a max reference value
