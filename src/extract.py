import pandas as pd

def extract_data(path):
    print("Extracting data...")
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = extract_data("s3_bucket/raw/sales_data.csv")
    print(df.head())
