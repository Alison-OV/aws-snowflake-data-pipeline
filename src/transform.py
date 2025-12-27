def transform_data(df):
    print("Transforming data...")

    df = df.dropna()
    df["total_amount"] = df["quantity"] * df["price"]
    df.columns = [c.upper() for c in df.columns]

    return df
