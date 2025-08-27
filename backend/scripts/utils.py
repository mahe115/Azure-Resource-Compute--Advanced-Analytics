# backend/scripts/utils.py
import pandas as pd
import numpy as np

def load_csv(path, parse_dates=['date']):
    return pd.read_csv(path, parse_dates=parse_dates)

def basic_cleaning(df):
    # standardize column names
    df = df.rename(columns=lambda x: x.strip().lower())
    # drop duplicates
    df = df.drop_duplicates()
    # ensure date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df

def impute_missing(df):
    # For numeric columns: forward fill then median
    numcols = df.select_dtypes(include='number').columns.tolist()
    df[numcols] = df[numcols].ffill().bfill()
    for c in numcols:
        if df[c].isnull().sum() > 0:
            df[c] = df[c].fillna(df[c].median())
    # For categorical: fill with mode or 'unknown'
    catcols = df.select_dtypes(exclude='number').columns.tolist()
    for c in catcols:
        df[c] = df[c].fillna(method='ffill').fillna('unknown')
    return df

def merge_datasets(azure_df, external_df, on=['date','region']):
    # try merging on date and region; if region missing, merge on date only
    try:
        merged = pd.merge(azure_df, external_df, how='left', on=on)
    except Exception:
        merged = pd.merge(azure_df, external_df, how='left', on='date')
    return merged

def save_df(df, path):
    df.to_csv(path, index=False)

# Feature engineering
def add_time_features(df, date_col='date'):
    df['day_of_week'] = df[date_col].dt.day_name()
    df['day_of_week_num'] = df[date_col].dt.dayofweek
    df['month'] = df[date_col].dt.month
    df['quarter'] = df[date_col].dt.quarter
    df['is_weekend'] = df[date_col].dt.dayofweek >= 5
    return df

def add_lag_roll_features(df, groupby_cols=['region'], target_col='usage_cpu'):
    df = df.sort_values(['region','date'])
    for lag in [1,3,7]:
        df[f'{target_col}_lag_{lag}'] = df.groupby(groupby_cols)[target_col].shift(lag)
    # rolling windows
    for win in [7,30]:
        df[f'{target_col}_roll_mean_{win}'] = df.groupby(groupby_cols)[target_col].transform(lambda x: x.rolling(win, min_periods=1).mean())
        df[f'{target_col}_roll_max_{win}'] = df.groupby(groupby_cols)[target_col].transform(lambda x: x.rolling(win, min_periods=1).max())
    return df

def add_ratio_features(df):
    # Ensure columns exist; names may vary in datasets, change if needed
    if 'cpu_total' in df.columns and 'cpu_used' in df.columns:
        df['cpu_utilization'] = df['cpu_used'] / df['cpu_total']
    elif 'usage_cpu' in df.columns:
        # assume usage_cpu is percent or actual - normalize if >1
        df['cpu_utilization'] = df['usage_cpu'].apply(lambda x: x/100 if x>1 else x)
    if 'storage_used' in df.columns and 'storage_allocated' in df.columns:
        df['storage_efficiency'] = df['storage_used'] / df['storage_allocated']
    return df
