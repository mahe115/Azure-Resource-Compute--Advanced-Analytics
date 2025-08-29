from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/usage-trends', methods=['GET'])
def get_usage_trends():
    df = pd.read_csv("data/processed/cleaned_merged.csv", parse_dates=['date'])
    data = df.groupby('date')['usage_cpu'].sum().reset_index()
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    forecast = [
        {"date": "2023-06-01", "predicted_cpu": 85},
        {"date": "2023-06-02", "predicted_cpu": 90},
        {"date": "2023-06-03", "predicted_cpu": 95},
    ]
    return jsonify(forecast)

if __name__ == '__main__':
    app.run(debug=True)