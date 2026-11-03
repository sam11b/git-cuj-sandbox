def clean_sales(df):
    """Remove bad rows before reporting."""
    df = df.dropna(subset=["order_id"])
    return df.filter(df["amount"] >= 0)
