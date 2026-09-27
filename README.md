# Week 2 Logistics Data Preprocessing

This project contains the Python implementation for the Week 2 Data Collection,
Cleaning and Preprocessing task.

## Dataset
Place the downloaded DataCo Smart Supply Chain CSV file in:

`data/raw/DataCoSupplyChainDataset.csv`

The dataset is publicly available through Kaggle:
https://www.kaggle.com/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python src/main.py
```

The cleaned dataset will be saved to:

`data/processed/DataCoSupplyChain_cleaned.csv`

## Project structure

- `src/data_loading.py` - loads and profiles the raw data
- `src/cleaning.py` - handles duplicates, missing values and data types
- `src/feature_engineering.py` - creates date and delivery features
- `src/preprocessing.py` - categorical encoding and numerical scaling
- `src/outlier_detection.py` - IQR-based outlier detection
- `src/validation.py` - final data-quality checks
- `src/main.py` - runs the complete pipeline
