# AZURE_BACKEND_TEAM-B


# 📝 EDA Report – Milestone 1

## 📅 Project: Azure Demand Forecasting  
**Milestone:** Data Collection & Preparation  
**Team:** Backend - B 
**Date:** 25-08-25


## 1. 📂 Datasets Used
- `azure_usage.csv`: Simulated data for Azure Compute & Storage usage  
- `external_factors.csv`: Economic indicators and cloud market demand

## 2. 📊 Key Observations

## Azure Usage:
- Number of records: 1080  
- Regions covered: East US, West US, Central US, North Europe, West Europe   
- Average CPU usage: 74.65  
- Average Storage usage: 1242.48  
- Active users range: 200 - 499  

### External Data:
- Economic Index range: 73.80 - 118.86  
- Market Demand: Mean = 1.01, Std Dev = 0.10  
- Holidays: Weekend indicator included

## 3. 🧼 Data Quality Checks

| Column              | Missing Values | Action Taken |
|---------------------|----------------|--------------|
| usage_cpu           | 0              | None         |
| usage_storage       | 0              | None         |
| users_active        | 0              | None         |
| economic_index      | 0              | None         |
| cloud_market_demand | 0              | None         |
| holiday             | 0              | None         |

No missing data encountered in either dataset; no imputation was necessary.

## 4. 📈 Visualizations

- **Total CPU usage trend over time**  :    
  Displays trends in Azure compute usage, showing periodic fluctuations and potential seasonality.

![alt text](<Screenshot 2025-08-23 170247.png>)

- **Region-wise average usage bar chart** :

  Highlights which geographic regions have higher average compute demands.

  ![alt text](<Screenshot 2025-08-23 170301.png>) ![alt text](<Screenshot 2025-08-23 170247-1.png>)


- Correlation heatmap :
  Insights into relationships between usage metrics and other numeric features, indicating possible predictive features.

 ![alt text](<Screenshot 2025-08-23 170313.png>)

## 5. 🧩 Merging External Data
Successfully merged internal and external datasets on `date`.

## 6. ✅ Final Output
Cleaned dataset saved at: `data/processed/cleaned_merged.csv`  
Ready for feature engineering.

---

## 📌 Notes / Challenges
- No missing data or datatype inconsistencies observed.  
- Future steps: in-depth feature engineering including temporal and regional effects, and leveraging external economic indicators.


## FOLDER_STRUCTURE

azure-demand-forecasting/
│
├── data/
│   ├── raw/
│   │   ├── azure_usage.csv
│   │   └── external_factors.csv
│   └── processed/
│       └── cleaned_merged.csv
│
├── notebooks/
│   ├── 01_data_loading_eda.ipynb
│   └── 02_data_cleaning_merging.ipynb
│
├── scripts/
│   └── utils.py
│
├── reports/
│   └── eda_report.md
│
├── requirements.txt
└── README.md
