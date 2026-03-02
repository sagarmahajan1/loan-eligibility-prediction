import streamlit as st
import joblib
import numpy as np

# Page Config
st.set_page_config(page_title="Loan Prediction App", page_icon="🏦", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        height: 3em;
        width: 100%;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Eligibility Prediction")
st.markdown("### Fill Applicant Details Below 👇")

with st.container():

    col1, col2 = st.columns(2)

    with col1:
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])

    with col2:
        property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
        credit_history = st.selectbox("Credit History", ["Good", "Bad"])
        loan_amount = st.number_input("Loan Amount")
        loan_term = st.number_input("Loan Term (Months)")
        income = st.number_input("Total Income")

# Encoding (SAME as training ⚠️)
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

dependents = 3 if dependents == "3+" else int(dependents)

property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]

credit_history = 1 if credit_history == "Good" else 0

# Prediction Button
if st.button("🔍 Check Eligibility"):

    input_data = np.array([[married,
                            dependents,
                            education,
                            self_employed,
                            loan_amount,
                            loan_term,
                            credit_history,
                            property_area,
                            income]])

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Congratulations! Loan Approved ✅")
    else:
        st.error("❌ Sorry! Loan Not Approved")