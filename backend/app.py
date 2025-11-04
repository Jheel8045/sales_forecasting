from flask import Flask, request, jsonify
import joblib
import pandas as pd
from prophet import Prophet

app = Flask(__name__)

# Load saved model
import os
model_path = os.path.join(os.path.dirname(__file__), "../model/prophet_model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return "✅ Sales Forecasting API is running!"

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        # Get number of future weeks from request JSON
        data = request.get_json()
        periods = data.get("periods", 12)

        # Generate future dates
        future = model.make_future_dataframe(periods=periods, freq='W')
        forecast = model.predict(future)

        # Prepare output
        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
        result_dict = result.to_dict(orient='records')
        return jsonify(result_dict)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
