import os
import pandas as pd
from flask import Blueprint, jsonify

data_bp = Blueprint("data", __name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
file_path = os.path.join(BASE_DIR, "Data", "Processed", "cleaned_merged.csv")

print("🔍 Loading file from:", file_path)

cleaned_data = pd.read_csv(file_path)

@data_bp.route("/raw-data", methods=["GET"])
def get_raw_data():
    return cleaned_data.head(len(cleaned_data)).to_dict(orient="records")
