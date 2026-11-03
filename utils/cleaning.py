def clean_sales(df):
    """Remove bad rows before reporting."""
    return df.dropna(subset=["order_id"])
