def clean_sales(df):
    """Drop rows with missing order IDs."""
    return df.dropna(subset=["order_id"])
