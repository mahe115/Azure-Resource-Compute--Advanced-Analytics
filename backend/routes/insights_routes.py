import os
import pandas as pd
from flask import Blueprint, jsonify

insights_bp = Blueprint("insights", __name__)

# ---------- Load dataset ----------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
file_path = os.path.join(BASE_DIR, "Data", "Processed", "cleaned_merged.csv")

df = pd.read_csv(file_path)
df["date"] = pd.to_datetime(df["date"])


# ---------- Helpers ----------
def safe_df(df):
    """Ensure DataFrame is JSON serializable"""
    df_copy = df.copy()

    for col in df_copy.columns:
        if pd.api.types.is_period_dtype(df_copy[col]):
            df_copy[col] = df_copy[col].astype(str)

    if isinstance(df_copy.columns, pd.MultiIndex):
        df_copy.columns = ["_".join([str(c) for c in col if c]) for col in df_copy.columns]

    return df_copy.reset_index().to_dict(orient="records")



def safe_value(val):
    """Convert numpy & pandas types to Python builtins"""
    if isinstance(val, (pd.Period,)):
        return str(val)
    if hasattr(val, "item"):  
        return val.item()
    return val


# ---------- Routes ----------

# 1. Usage trends (avg CPU per region)
@insights_bp.route("/usage-trends", methods=["GET"])
def usage_trends():
    trends = df.groupby("region")["usage_cpu"].mean().round(2).reset_index()
    return safe_df(trends)


# 2. Top regions by demand
@insights_bp.route("/top-regions", methods=["GET"])
def top_regions():
    top = (
        df.groupby("region")["usage_cpu"]
        .sum()
        .reset_index()
        .sort_values(by="usage_cpu", ascending=False)
        .head(5)
    )
    return safe_df(top)


# 3. Peak demand per month
@insights_bp.route("/peak-demand", methods=["GET"])
def peak_demand():
    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M").astype(str)
    monthly = df_copy.groupby("month")["usage_cpu"].max().reset_index()
    return safe_df(monthly)


# 4. Regional comparison (flattened columns)
@insights_bp.route("/regional-comparison", methods=["GET"])
def regional_comparison():
    comparison = (
        df.groupby("region")
        .agg({
            "usage_cpu": ["mean", "max", "std"],
            "usage_storage": ["mean", "max", "std"],
            "users_active": ["mean", "max", "std"]
        })
        .round(2)
    )
    return safe_df(comparison)


# 5. Holiday vs Non-holiday impact
@insights_bp.route("/holiday-impact", methods=["GET"])
def holiday_impact():
    if "holiday" not in df.columns:
        return jsonify({"error": "holiday column not found in dataset"}), 400

    holiday_stats = (
        df.groupby("holiday")
        .agg({
            "usage_cpu": "mean",
            "usage_storage": "mean",
            "users_active": "mean",
            "cloud_market_demand": "mean" if "cloud_market_demand" in df.columns else "mean"
        })
        .round(2)
    )
    return safe_df(holiday_stats)


# 6. Monthly trends
@insights_bp.route("/monthly-trends", methods=["GET"])
def monthly_trends():
    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M").astype(str)
    monthly = (
        df_copy.groupby(["month", "region", "resource_type"])
        .agg({
            "usage_cpu": "mean",
            "usage_storage": "mean",
            "users_active": "mean"
        })
        .round(2)
        .reset_index()
    )
    return safe_df(monthly)


# 7. Insights summary
@insights_bp.route("/insights", methods=["GET"])
def insights():
    summary = {
        "avg_cpu_usage": safe_value(df["usage_cpu"].mean().round(2)),
        "peak_usage": safe_value(df["usage_cpu"].max()),
        "total_records": int(len(df)),
        "top_region": str(df.groupby("region")["usage_cpu"].mean().idxmax())
    }
    return jsonify(summary)

# 8. Insights summary for storage
@insights_bp.route("/insights-storage", methods=["GET"])
def storage_insights():
    summary = {
        "avg_storage_usage": safe_value(df["usage_storage"].mean().round(2)),
        "peak_usage": safe_value(df["usage_storage"].max()),
        "total_records": int(len(df)),
        "top_region": str(df.groupby("region")["usage_storage"].mean().idxmax())
    }
    return jsonify(summary)

# 9. Usage trends (avg storage per region)
@insights_bp.route("/usage-trends-storage", methods=["GET"])
def storage_usage_trends():
    trends = df.groupby("region")["usage_storage"].mean().round(2).reset_index()
    return safe_df(trends)

# 10. Top regions by storage demand
@insights_bp.route("/top-regions-storage", methods=["GET"])
def storage_top_regions():
    top = (
        df.groupby("region")["usage_storage"]
        .sum()
        .reset_index()
        .sort_values(by="usage_storage", ascending=False)
        .head(5)
    )
    return safe_df(top)


# 11. Peak storage demand per month
@insights_bp.route("/peak-demand-storage", methods=["GET"])
def storage_peak_demand():
    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M").astype(str)
    monthly = df_copy.groupby("month")["usage_storage"].max().reset_index()
    return safe_df(monthly)