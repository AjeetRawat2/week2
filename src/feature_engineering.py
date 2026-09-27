import pandas as pd


def create_features(df):
    """Create time and delivery-related features."""
    data = df.copy()

    date_col = "order date (DateOrders)"

    if date_col in data.columns:
        data["order_year"] = data[date_col].dt.year
        data["order_month"] = data[date_col].dt.month
        data["order_day"] = data[date_col].dt.day
        data["order_dayofweek"] = data[date_col].dt.dayofweek

    if (
        "Days for shipping (real)" in data.columns
        and "Days for shipment (scheduled)" in data.columns
    ):
        data["delivery_days"] = data["Days for shipping (real)"]

        data["delivery_delay"] = (
            data["Days for shipping (real)"]
            - data["Days for shipment (scheduled)"]
        )

    return data
