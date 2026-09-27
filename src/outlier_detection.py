import pandas as pd


def detect_iqr_outliers(df, column, multiplier=1.5):
    """Return rows outside the IQR limits for a numerical column."""
    if column not in df.columns:
        raise KeyError(f"Column not found: {column}")

    series = pd.to_numeric(df[column], errors="coerce").dropna()

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr

    mask = (
        (pd.to_numeric(df[column], errors="coerce") < lower)
        | (pd.to_numeric(df[column], errors="coerce") > upper)
    )

    return df[mask].copy(), lower, upper


def report_outliers(df, columns):
    """Print an outlier summary without deleting any observations."""
    print("\n--- OUTLIER REPORT ---")

    for column in columns:
        if column not in df.columns:
            continue

        outliers, lower, upper = detect_iqr_outliers(df, column)

        print(
            f"{column}: {len(outliers)} possible outliers | "
            f"lower={lower:.3f}, upper={upper:.3f}"
        )
