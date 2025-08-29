# 📝 EDA Report – Milestone 1

## 📅 Project: Azure Demand Forecasting  
**Milestone:** Data Collection & Preparation  
**Team:** Backend - B  
**Date:** 2023-08-25

## 1. 📂 Datasets Used
### Azure Usage Data (azure_usage.csv)
- Daily compute and storage usage metrics
- Regional distribution data
- Resource utilization patterns
- User activity metrics

### External Factors (external_factors.csv)
- Economic indicators
- Market demand metrics
- Holiday/Weekend flags

## 2. 📊 Key Observations
### Azure Usage Patterns:
- Records analyzed: Daily data from Merged_Data.csv
- Regions covered: East US, West US, North Europe, Southeast Asia
- CPU Utilization: 
  - Shows distinct patterns by resource type
  - Daily averages vary significantly between regions
  - Clear temporal trends visible in time series analysis
- Storage Usage: 
  - Box plot analysis shows varying distributions by region
  - Resource types have different storage patterns
  - Regional averages range significantly (documented in statistical summary)
- User Activity: 
  - Clear regional variations in active user counts
  - Temporal patterns follow business cycles

### External Factors Analysis:
- Economic index shows strong correlation with cloud market demand
- Holiday periods show distinct usage patterns
- Clear relationship between economic indicators and resource utilization

## 3. 🧼 Data Quality Checks
- Missing values: None
- Duplicates: None
- Consistency: Ensured across merged dataset
- Outliers: Identified and handled

## 4. 📈 Key Visualizations
### Generated Visualizations
1. Resource Usage Analysis
   - CPU usage trends by resource type (time series)
   - Daily average CPU usage by region
   - Storage usage distribution by region and resource type (box plots)

2. User Activity Analysis
   - Active users over time by region
   - Regional comparison of user patterns

3. Resource Distribution Analysis
   - Resource allocation patterns by region
   - Average CPU usage by region and resource type

4. Economic Impact Analysis
   - Economic index vs cloud demand scatter plot
   - Holiday impact visualization

5. Correlation Analysis
   - Usage metrics correlation heatmap showing:
     - Strong correlation between CPU and storage usage
     - User activity correlations with resource metrics

### Key Findings from Visualizations
- Resource utilization shows clear regional patterns
- Holiday periods significantly impact usage metrics
- Strong correlations between usage metrics indicate consistent patterns
- Economic indicators correlate with cloud demand patterns

## 5. Data Integration
- Successfully merged usage and external data
- Temporal alignment confirmed
- No data loss during integration

## 6. Outputs
- Clean dataset: `Data/Processed/cleaned_merged.csv`
- Documentation complete

## Technical Notes
1. Data preprocessing complete
2. Baseline metrics established

---
