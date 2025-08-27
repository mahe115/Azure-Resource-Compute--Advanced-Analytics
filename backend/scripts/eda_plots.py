# backend/scripts/eda_plots.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

sns.set(style="whitegrid")
ROOT = Path(__file__).resolve().parents[1]   # .../backend/scripts -> parents[1] = backend
PROC = ROOT / "data" / "processed"
OUT = ROOT / "reports" / "images"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PROC / "merged.csv")
df['date'] = pd.to_datetime(df['date'])
print("Loaded merged.csv with shape:", df.shape)

# List of plots (same code as notebook - wrapped as functions)
def save_plot_cpu_trend():
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x="date", y="usage_cpu", hue="region", estimator='mean')
    plt.title("Azure CPU Usage Over Time by Region")
    plt.xlabel("Date")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.02,1), loc='upper left')
    plt.tight_layout()
    plt.savefig(OUT / "cpu_usage_trend_by_region.png", dpi=150, bbox_inches="tight")
    plt.close()

def save_plot_storage_trend():
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x="date", y="usage_storage", hue="region", estimator='mean')
    plt.title("Azure Storage Usage Over Time by Region")
    plt.xlabel("Date")
    plt.ylabel("Storage Usage")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.02,1), loc='upper left')
    plt.tight_layout()
    plt.savefig(OUT / "storage_usage_trend_by_region.png", dpi=150, bbox_inches="tight")
    plt.close()

def save_plot_avg_cpu_region():
    avg_cpu = df.groupby("region")["usage_cpu"].mean().sort_values(ascending=False).reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(data=avg_cpu, x="region", y="usage_cpu")
    plt.title("Average CPU Usage by Region")
    plt.xlabel("Region")
    plt.ylabel("Average CPU Usage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUT / "avg_cpu_by_region.png", dpi=150, bbox_inches="tight")
    plt.close()

def save_plot_corr():
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap (numeric features)")
    plt.tight_layout()
    plt.savefig(OUT / "correlation_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()

def save_boxplot_cpu_region():
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df, x="region", y="usage_cpu")
    plt.title("Region-wise CPU Usage Distribution")
    plt.xlabel("Region")
    plt.ylabel("CPU Usage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUT / "cpu_boxplot_by_region.png", dpi=150, bbox_inches="tight")
    plt.close()

def save_monthly_avg():
    df['month'] = df['date'].dt.month
    monthly = df.groupby('month')['usage_cpu'].mean().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(data=monthly, x='month', y='usage_cpu', marker='o')
    plt.title("Monthly Avg CPU Usage")
    plt.xlabel("Month")
    plt.ylabel("Avg CPU Usage (%)")
    plt.xticks(range(1,13))
    plt.tight_layout()
    plt.savefig(OUT / "monthly_avg_cpu.png", dpi=150, bbox_inches="tight")
    plt.close()

# run all
save_plot_cpu_trend()
save_plot_storage_trend()
save_plot_avg_cpu_region()
save_plot_corr()
save_boxplot_cpu_region()
save_monthly_avg()
print("Saved plots to:", OUT)
