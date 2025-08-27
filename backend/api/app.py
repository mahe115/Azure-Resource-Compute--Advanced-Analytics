'''# backend/api/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from pathlib import Path

app = Flask(__name__)
CORS(app)

PROC = Path(__file__).resolve().parents[1] / "data" / "processed"

def _load_cleaned():
    path = PROC / "cleaned_merged.csv"
    return pd.read_csv(path, parse_dates=['date']) if path.exists() else pd.DataFrame()

def _load_features():
    path = PROC / "feature_engineered.csv"
    return pd.read_csv(path, parse_dates=['date']) if path.exists() else pd.DataFrame()

@app.route('/api/usage-trends')
def usage_trends():
    df = _load_cleaned()
    # optional query: region
    region = request.args.get('region')
    if region:
        df = df[df['region']==region]
    trends = df.groupby('date')['usage_cpu'].mean().reset_index()
    trends['date'] = trends['date'].dt.strftime('%Y-%m-%d')
    return jsonify(trends.to_dict(orient='records'))

@app.route('/api/top-regions')
def top_regions():
    df = _load_cleaned()
    top = df.groupby("region")["usage_cpu"].mean().sort_values(ascending=False).head(10).reset_index()
    return jsonify(top.to_dict(orient='records'))

@app.route('/api/raw-data')
def raw_data():
    df = _load_cleaned()
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/features')
def features():
    df = _load_features()
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/insights')
def insights():
    df = _load_features()
    if df.empty:
        return jsonify({"message":"no data"}), 400
    peak_usage = float(df['usage_cpu'].max())
    top_region = df.groupby('region')['usage_cpu'].mean().idxmax()
    avg_storage_eff = float(df['storage_efficiency'].mean()) if 'storage_efficiency' in df.columns else None
    return jsonify({
        "peak_usage": peak_usage,
        "top_region": top_region,
        "avg_storage_efficiency": avg_storage_eff
    })
# Root route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to Azure Backend API! 🚀"})

# Example API route
@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "pong"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
'''
# backend/api/app.py
import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from pathlib import Path

app = Flask(__name__)
CORS(app)
print("🔹 Azure Backend API is starting...")


# Paths
PROC = Path(__file__).resolve().parents[1] / "data" / "processed"

# Helpers
def _load_cleaned():
    """Load cleaned merged CSV as a DataFrame"""
    path = PROC / "cleaned_merged.csv"
    return pd.read_csv(path, parse_dates=['date']) if path.exists() else pd.DataFrame()



def _load_features():
    """Load feature-engineered CSV as a DataFrame"""
    path = PROC / "feature_engineered.csv"
    return pd.read_csv(path, parse_dates=['date']) if path.exists() else pd.DataFrame()

# Routes

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Azure Backend API! 🚀"})

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "pong"})

# Milestone 1 APIs
@app.route('/api/usage-trends')
def usage_trends():
    logging.info("Usage trends API called") 
    df = _load_cleaned()
    region = request.args.get('region')
    if region:
        df = df[df['region'] == region]
    if df.empty:
        return jsonify({"message": "No data found"}), 400
    trends = df.groupby('date')['usage_cpu'].mean().reset_index()
    trends['date'] = trends['date'].dt.strftime('%Y-%m-%d')
    return jsonify(trends.to_dict(orient='records'))


@app.route('/api/top-regions')
def top_regions():
    df = _load_cleaned()
    if df.empty:
        return jsonify({"message": "No data found"}), 400
    top = (
        df.groupby("region")["usage_cpu"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    return jsonify(top.to_dict(orient='records'))

@app.route('/api/raw-data')
def raw_data():
    df = _load_cleaned()
    if df.empty:
        return jsonify({"message": "No data found"}), 400
    return jsonify(df.to_dict(orient='records'))

# Milestone 2 APIs
@app.route('/api/features')
def features():
    df = _load_features()
    if df.empty:
        return jsonify({"message": "No data found"}), 400
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/insights')
def insights():
    df = _load_features()
    if df.empty:
        return jsonify({"message": "No data found"}), 400

    peak_usage = float(df['usage_cpu'].max())
    top_region = df.groupby('region')['usage_cpu'].mean().idxmax()
    avg_storage_eff = (
        float(df['storage_efficiency'].mean())
        if 'storage_efficiency' in df.columns
        else None
    )

    return jsonify({
        "peak_usage": peak_usage,
        "top_region": top_region,
        "avg_storage_efficiency": avg_storage_eff
    })

# Run App
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
