import pandas as pd
from sklearn.preprocessing import StandardScaler


def encode_categories(df, categorical_columns):
    """One-hot encode selected categorical columns."""
    columns = [c for c in categorical_columns if c in df.columns]

    if not columns:
        return df.copy()

    return pd.get_dummies(
        df,
        columns=columns,
        drop_first=True,
        dtype=int
    )


def scale_numeric_features(df, numeric_columns):
    """Standardize selected numerical features using StandardScaler."""
    columns = [c for c in numeric_columns if c in df.columns]

    result = df.copy()

    if not columns:
        return result, None

    valid = result[columns].dropna()

    scaler = StandardScaler()
    scaled = scaler.fit_transform(valid)

    scaled_df = pd.DataFrame(
        scaled,
        columns=columns,
        index=valid.index
    )

    result.loc[valid.index, columns] = scaled_df

    return result, scaler
