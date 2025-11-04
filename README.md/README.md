# 📊 Sales Forecasting App

A full-stack **Sales Forecasting Dashboard** built using **Prophet**, **Flask**, and **Streamlit**.  
This project predicts future sales trends using historical data and presents interactive visualizations for business insights.

## 🚀 Features

- 🧠 Time-series forecasting using **Facebook Prophet**
- 🗃️ Clean modular folder structure (data, model, backend, frontend)
- 🌐 REST API built with **Flask**
- 📈 Interactive dashboard built with **Streamlit** + **Plotly**
- 🔍 Weekly forecast visualizations and tabular insights
- 💾 Local model storage using `joblib`

## 🗂️ Project Structure

sales_forecasting/
│
├── data/ # Raw + processed data
├── notebooks/ # Jupyter/Colab notebooks
├── model/ # Trained Prophet model, saved forecast files
├── backend/ # Flask API
│ ├── app.py
│ └── requirements.txt
├── frontend/ # Streamlit dashboard
│ ├── dashboard.py
│ └── requirements.txt
└── README.md

## ⚙️ Installation

### 1️⃣ Clone the Repository
https://github.com/Jheel8045/sales_forecasting.git
cd sales_forecasting

### 2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate      # for Windows
source venv/bin/activate   # for macOS/Linux

### 3️⃣ Install Dependencies
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

### ▶️ Run the Application
Step 1:Start the Flask backend
cd backend
python app.py

Step 2:Start the Streamlit frontend
open a new terminal
cd frontend
streamlit run dashboard.py

### 📊 Example Output
Forecast table with predicted sales for coming weeks
Line graph showing sales trend (Plotly Interactive Chart)
Adjustable forecast period (1–52 weeks)

### 🧠 Technologies Used
Data Science:	Prophet, Pandas, NumPy
Backend :API Flask, Requests
Frontend UI	: Streamlit, Plotly
Model Saving : Joblib
Version Control :	Git, GitHub 
Deployment :
Deployed backend on RENDER.
Deployed Streamlit frontend on RENDER.

### 🚀 Live Demo
https://sales-forecasting-1-o94l.onrender.com/

### 👩‍💻 Author
Jheel Jain
📍 Jabalpur, Madhya Pradesh
🔗 GitHub - https://github.com/Jheel8045

### 📜 License
This project is licensed under the MIT License.
