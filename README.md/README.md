# 🧠 Sales Forecasting using Prophet + Flask + Streamlit

A complete **end-to-end Machine Learning project** that predicts weekly retail sales using the **Facebook Prophet** model.  
This project includes **data preprocessing, model training, API deployment, and a Streamlit dashboard** for visualization.

---

## 📊 Project Overview

The goal of this project is to forecast weekly sales based on retail transaction data.  
We used multiple datasets (calendar, customers, products, stores, and sales data) and applied time-series forecasting.

### Key Features
✅ Data preprocessing and feature engineering  
✅ Prophet model for time-series forecasting  
✅ Flask backend API for prediction requests  
✅ Streamlit dashboard for visualization  
✅ Modular folder structure (scalable and deployable)

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend (UI)** | Streamlit |
| **Backend (API)** | Flask |
| **Modeling** | Prophet, Pandas, NumPy |
| **Visualization** | Plotly |
| **Environment** | Python 3.13 |

---

## 📂 Folder Structure
sales_forecasting/
│
├── data/ # raw + processed datasets
├── notebooks/ # model training notebooks
│ └── sales_forecasting_final.ipynb
├── model/ # saved Prophet model
│ └── prophet_model.pkl
├── backend/ # Flask API
│ ├── app.py
│ └── requirements.txt
├── frontend/ # Streamlit dashboard
│ └── dashboard.py
└── README.md
