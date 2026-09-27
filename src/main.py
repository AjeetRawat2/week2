from pathlib import Path

from data_loading import load_data, profile_data
from cleaning import clean_data
from outlier_detection import report_outliers
from feature_engineering import create_features
from preprocessing import encode_categories, scale_numeric_features
from validation import validate_data


RAW_FILE = Path("data/raw/DataCoSupplyChainDataset.csv")
OUTPUT_FILE = Path("data/processed/DataCoSupplyChain_cleaned.csv")


def main():
    print("Starting Week 2 logistics preprocessing pipeline...")

    # 1. Load
    df = load_data(RAW_FILE)
    profile_data(df)

    # 2. Clean
    clean = clean_data(df)

    # 3. Detect possible outliers
    report_outliers(
        clean,
        [
            "Order Item Quantity",
            "Sales",
            "Order Item Product Price"
        ]
    )

    # 4. Feature engineering
    clean = create_features(clean)

    # 5. Encode selected categories
    clean = encode_categories(
        clean,
        [
            "Shipping Mode",
            "Market",
            "Order Region"
        ]
    )

    # 6. Save the cleaned analysis dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(OUTPUT_FILE, index=False)

    # 7. Final validation
    validate_data(clean)

    print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
