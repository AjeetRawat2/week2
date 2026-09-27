import pandas as pd


def clean_data(df):
    """Apply basic data-quality cleaning while preserving the original dataframe."""
    clean = df.copy()

    # Remove exact duplicate rows.
    duplicate_count = clean.duplicated().sum()
    clean = clean.drop_duplicates().copy()

    # Convert date fields when they are available.
    date_columns = [
        "order date (DateOrders)",
        "shipping date (DateOrders)"
    ]

    for col in date_columns:
        if col in clean.columns:
            clean[col] = pd.to_datetime(clean[col], errors="coerce")

    # Convert important numerical fields.
    numeric_columns = [
        "Sales",
        "Order Item Quantity",
        "Order Item Discount Rate",
        "Order Item Product Price",
        "Days for shipping (real)",
        "Days for shipment (scheduled)"
    ]

    for col in numeric_columns:
        if col in clean.columns:
            clean[col] = pd.to_numeric(clean[col], errors="coerce")

    # Fill selected categorical missing values.
    categorical_columns = [
        "Shipping Mode",
        "Market",
        "Order Region",
        "Category Name"
    ]

    for col in categorical_columns:
        if col in clean.columns:
            clean[col] = clean[col].fillna("Unknown")

    # Fill a numerical demand field with its median where appropriate.
    if "Order Item Quantity" in clean.columns:
        median_quantity = clean["Order Item Quantity"].median()
        clean["Order Item Quantity"] = clean["Order Item Quantity"].fillna(
            median_quantity
        )

    # Standardize text fields.
    text_columns = [
        "Shipping Mode",
        "Market",
        "Order Region",
        "Category Name"
    ]

    for col in text_columns:
        if col in clean.columns:
            clean[col] = (
                clean[col]
                .astype("string")
                .str.strip()
            )

    print(f"Duplicate rows removed: {duplicate_count}")
    return clean
