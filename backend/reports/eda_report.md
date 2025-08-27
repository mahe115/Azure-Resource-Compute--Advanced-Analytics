# EDA Report – Milestone 1 & 2

## Datasets
- `azure_usage.csv` (raw) — rows: <fill_count>, cols: <fill_count>
- `external_factors.csv` (raw) — rows: <fill_count>, cols: <fill_count>
- `cleaned_merged.csv` (processed) — rows: <fill_count>, cols: <fill_count>
- `feature_engineered.csv` (final features) — rows: <fill_count>, cols: <fill_count>

---

## Data cleaning steps
- Removed duplicates: <n>
- Missing values handled: columns and method (e.g., `usage_storage` imputed with median)
- Date standardized to `YYYY-MM-DD`
- Units normalized: CPU → fraction (0-1) or percent, Storage → GB

---

## Milestone 1 Results
- Avg daily CPU usage (overall): `<value>`
- Peak demand month: `<month year>`
- Top 5 regions by avg usage: 1) A 2) B 3) C 4) D 5) E

**Plots created**
1. `reports/cpu_usage_trend.png` — CPU usage over time (line)
2. `reports/storage_consumption.png` — Storage consumption by region (bar)
3. `reports/region_share.png` — Region-wise demand (pie)

---

## Milestone 2 — Feature Engineering
**Features added**
- `day_of_week`, `month`, `quarter`, `is_weekend`
- `usage_cpu_lag_1`, `usage_cpu_lag_3`, `usage_cpu_lag_7`
- `usage_cpu_roll7_mean`, `usage_cpu_roll30_mean`
- `utilization_ratio`, `storage_efficiency`

**Justification**
- Lags & rolling stats capture temporal autocorrelation and smoothing for forecasting.
- Derived metrics help with capacity planning KPIs.

**Saved file**
- `data/processed/feature_engineered.csv`

**Plots created**
4. `reports/feature_correlation_heatmap.png` — correlations heatmap
5. `reports/region_boxplots.png` — region-wise distribution per resource
6. `reports/seasonality_monthly.png` — monthly seasonality trend

---

## Key insights & next steps
- Weekly seasonality: weekdays > weekends.
- Top growth regions: `RegionX`, `RegionY`.
- Storage efficiency highest in: `RegionZ`.
- Next: Build and evaluate forecasting model (ARIMA/LSTM/Prophet/XGBoost), create capacity planning rules, and wire frontend dashboard to `/api/features` and `/api/insights`.
