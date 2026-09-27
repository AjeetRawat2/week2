import pandas as pd


def validate_data(df):
    """Run final data-quality checks."""
    print("\n--- FINAL VALIDATION ---")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Duplicate rows:", df.duplicated().sum())

    missing = df.isna().sum().sort_values(ascending=False)
    print("\nTop remaining missing values:")
    print(missing.head(10))

    print("\nNumeric columns:")
    print(df.select_dtypes(include="number").columns.tolist())

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": int(df.duplicated().sum()),
        "missing_values": int(df.isna().sum().sum())
    }
