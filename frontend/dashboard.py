import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("📈 Sales Forecast Dashboard")

# Input section
periods = st.number_input("Forecast Weeks Ahead", min_value=1, max_value=52, value=7)

if st.button("Generate Forecast"):
    # Send request to Flask backend
    response = requests.post("http://127.0.0.1:5000/forecast", json={"periods": periods})
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # Plot forecast
        fig = px.line(df, x="ds", y="yhat", title=f"{periods}-Week Forecast")
        st.plotly_chart(fig)
        st.dataframe(df)
    else:
        st.error("Error fetching forecast. Check if Flask server is running.")
