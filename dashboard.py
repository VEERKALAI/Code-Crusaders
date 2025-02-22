import streamlit as st
import pandas as pd
import requests

st.title("🔍 Real-Time Fraud Detection Dashboard")

# Load transaction data (Optional)
try:
    df = pd.read_csv("transactions.csv")  # Ensure this file exists
    st.dataframe(df)
except FileNotFoundError:
    st.error("⚠️ transactions.csv not found! Please provide a valid dataset.")

# User input form for entering transaction details
st.subheader("📌 Enter Transaction Details:")
amount = st.number_input("Transaction Amount", min_value=1)
transaction_type = st.selectbox("Transaction Type", [1, 2, 3])  # Assume types (1: Online, 2: ATM, 3: Bank Transfer)
user_id = st.number_input("User ID", min_value=100, max_value=999)

# API URL (Make sure FastAPI is running)
API_URL = "http://127.0.0.1:8000/detect_fraud/"

if st.button("Detect Fraud"):
    transaction_data = {
        "Amount": amount,
        "Transaction_Type": transaction_type,
        "User_ID": user_id
    }

    # Send transaction data to API
    response = requests.post(API_URL, json=transaction_data)

    # Handle response
    if response.status_code == 200:
        result = response.json()
        if result["Fraud"]:
            st.error("🚨 FRAUD DETECTED! This transaction is suspicious.")
        else:
            st.success(" Transaction is Fraud!! Be safe the hackers may hack your account.")
    else:
        st.error("⚠️ Error communicating with API. Please check API connection.")
