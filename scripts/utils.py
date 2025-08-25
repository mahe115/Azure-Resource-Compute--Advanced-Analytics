import pandas as pd

def load_data():
    azure_df = pd.read_csv("../data/raw/azure_usage.csv")
    external_df = pd.read_csv("../data/raw/external_factors.csv")
    azure_df['date'] = pd.to_datetime(azure_df['date'])
    external_df['date'] = pd.to_datetime(external_df['date'])
    return azure_df, external_df

def merge_data(azure_df, external_df):
    return pd.merge(azure_df,external_df,on='date',how='left')

def load_processed_data(path='../data/processed/cleaned_merged.csv'):
    return pd.read_csv(path,parse_dates=['date'])