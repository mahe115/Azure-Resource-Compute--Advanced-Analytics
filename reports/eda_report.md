# EDA Report – Azure Usage & External Factors

## Dataset Overview
- Azure dataset contains:
  - Fields: `date`, `region`, `resource_type`, `usage_cpu`, `usage_storage`, `users_active`
  - Covers daily usage data by region and VM type.

- External dataset contains:
  - Fields: `date`, `economic_index`, `cloud_market_demand`, `holiday`
  - Captures macroeconomic and seasonal effects.

## Findings
- CPU usage shows clear time trends and variability by region.
- Storage and CPU usage are moderately correlated (~0.65).
- Active users strongly correlate with CPU usage (~0.72).
- External demand index trends upward, aligning with cloud adoption growth.

## Data Quality
- Minor missing values handled via imputation (median for numeric, mode for categorical).
- Datasets successfully merged on `date`.
