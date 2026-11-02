def clean_sales(df):
    """Drop rows with null order IDs."""
    return df.dropna(subset=["order_id"])
