import pandas as pd

# file_path = "data/transactions_dataset.parquet"
file_path = "data/transactions_dataset_reduced.parquet"

def read_and_process_parquet():
    df = pd.read_parquet(file_path)
    df['date_order'] = pd.to_datetime(df['date_order'])
    df['date_invoice'] = pd.to_datetime(df['date_invoice'])
    return df