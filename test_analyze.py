"""Unit tests for analyze.py"""
import pytest
from pathlib import Path
import sys
import tempfile
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from generate_data import generate_retail_data
from analyze import summary_statistics, filter_and_slice


@pytest.fixture
def sample_df():
    return generate_retail_data(n=200, seed=0)


def test_summary_stats_shape(sample_df):
    stats = summary_statistics(sample_df)
    assert stats.shape == (6, 6)   # 6 metrics x 6 numeric columns


def test_summary_stats_index(sample_df):
    stats = summary_statistics(sample_df)
    assert list(stats.index) == ['mean', 'median', 'min', 'max', 'count', 'std']


def test_filter_electronics_high(sample_df):
    with tempfile.TemporaryDirectory() as tmp:
        results = filter_and_slice(sample_df, Path(tmp))
    filtered = results['electronics_high_value']
    assert (filtered['Revenue'] > 10_000).all()


def test_filter_discounted(sample_df):
    with tempfile.TemporaryDirectory() as tmp:
        results = filter_and_slice(sample_df, Path(tmp))
    disc = results['discounted_orders']
    assert (disc['Discount'] >= 0.15).all()


def test_category_summary_columns(sample_df):
    with tempfile.TemporaryDirectory() as tmp:
        results = filter_and_slice(sample_df, Path(tmp))
    cols = results['category_summary'].columns.tolist()
    assert 'TotalRevenue' in cols and 'AvgRating' in cols


def test_monthly_trend_months(sample_df):
    with tempfile.TemporaryDirectory() as tmp:
        results = filter_and_slice(sample_df, Path(tmp))
    assert len(results['monthly_trend']) == 12
