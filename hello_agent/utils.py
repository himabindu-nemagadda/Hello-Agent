import pandas as pd


def calculate_data(df, operation, column=""):

    if operation == "count":
        return str(len(df))

    if operation not in ["sum", "mean", "min", "max"]:
        return "Unsupported operation."

    if column not in df.columns:
        return "Column not found."

    if not pd.api.types.is_numeric_dtype(df[column]):
        return "Column is not numeric."

    if df[column].dropna().empty:
        return "No numeric values available."

    operations = {
        "sum": df[column].sum,
        "mean": df[column].mean,
        "min": df[column].min,
        "max": df[column].max
    }

    return str(operations[operation]())

