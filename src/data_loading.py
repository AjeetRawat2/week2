import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/DataCoSupplyChainDataset.csv")


def load_data(file_path=RAW_FILE):
    """Load the raw DataCo supply-chain CSV file."""
    if not Path(file_path).exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}\n"
            "Place DataCoSupplyChainDataset.csv inside data/raw/"
        )

    df = pd.read_csv(file_path, encoding="latin-1")
    return df


def profile_data(df):
    """Print a basic profile of the dataset."""
    print("\n--- DATA PROFILE ---")
    print("Shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)

    print("\nTop missing-value counts:")
    print(df.isna().sum().sort_values(ascending=False).head(15))

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nNumerical summary:")
    print(df.describe().T)
