# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_core.ipynb (unless otherwise specified).

__all__ = ['display_large']

# Cell
import pandas as pd

# Cell
def display_large(df):
    """Displays up to 1000 columns and rows of pandas.DataFrame or pandas.Series objects."""
    with pd.option_context("display.max_rows", 1000, "display.max_columns", 1000):
        display(df)