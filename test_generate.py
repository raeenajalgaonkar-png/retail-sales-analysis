"""Unit tests for generate_data.py"""
import pandas as pd
import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from generate_data import generate_retail_data


def test_row_count():
    df = generate_retail_data(n=100)
    assert len(df) == 100


def test_required_columns():
    expected = {'OrderID', 'Date', 'Category', 'Product', 'Region',
                'Quantity', 'UnitPrice', 'Discount', 'PaymentMethod',
                'CustomerAge', 'Rating', 'Revenue', 'Month', 'Quarter'}
    df = generate_retail_data(n=50)
    assert expected.issubset(df.columns)


def test_revenue_calculation():
    df = generate_retail_data(n=50)
    expected = (df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])).round(2)
    pd.testing.assert_series_equal(df['Revenue'], expected, check_names=False)


def test_no_negative_values():
    df = generate_retail_data(n=200)
    assert (df['Revenue'] >= 0).all()
    assert (df['Quantity'] >= 1).all()
    assert (df['Discount'] >= 0).all()


def test_discount_valid_range():
    df = generate_retail_data(n=200)
    assert df['Discount'].between(0, 0.20).all()


def test_rating_range():
    df = generate_retail_data(n=200)
    assert df['Rating'].between(1, 5).all()
