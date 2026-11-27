import pandas as pd
import pytest

from utils import calculate_data


@pytest.fixture
def sales_dataframe():
    return pd.DataFrame({"Sales": [100, 200, 300]})


def test_sum(sales_dataframe):
    assert calculate_data(sales_dataframe, "sum", "Sales") == "600"


def test_mean(sales_dataframe):
    assert calculate_data(sales_dataframe, "mean", "Sales") == "200.0"


def test_count(sales_dataframe):
    assert calculate_data(sales_dataframe, "count") == "3"


def test_min(sales_dataframe):
    assert calculate_data(sales_dataframe, "min", "Sales") == "100"


def test_max(sales_dataframe):
    assert calculate_data(sales_dataframe, "max", "Sales") == "300"


def test_invalid_column(sales_dataframe):
    assert calculate_data(sales_dataframe, "sum", "Profit") == "Column not found."


def test_non_numeric_column():
    dataframe = pd.DataFrame({"Product": ["Laptop", "Mobile"]})

    assert calculate_data(dataframe, "sum", "Product") == "Column is not numeric."


def test_empty_numeric_column():
    dataframe = pd.DataFrame({"Sales": pd.Series([], dtype=float)})

    assert (
        calculate_data(dataframe, "mean", "Sales")
        == "No numeric values available."
    )


def test_unsupported_operation(sales_dataframe):
    assert (
        calculate_data(sales_dataframe, "divide", "Sales")
        == "Unsupported operation."
    )
