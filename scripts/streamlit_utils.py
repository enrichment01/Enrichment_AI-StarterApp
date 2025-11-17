"""
Streamlit utilities and data generation functions.
Extracted from pages/streamlit_basics.py
"""
import pandas as pd
import numpy as np


def generate_sample_dataframe():
    """Generate a sample DataFrame for demonstration."""
    return pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']
    })


def generate_random_data(num_rows, num_cols):
    """Generate random data for charts and tables."""
    return pd.DataFrame(
        np.random.randn(num_rows, num_cols),
        columns=[f'Column {i+1}' for i in range(num_cols)]
    )


def generate_chart_data(num_points=20, num_series=3):
    """Generate random data for chart demonstrations."""
    return pd.DataFrame(
        np.random.randn(num_points, num_series),
        columns=['A', 'B', 'C'][:num_series]
    )
