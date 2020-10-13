import pandas as pd

COLS_TO_DROP = []

def _drop_columns(df: pd.DataFrame, drop_cols: list) -> pd.DataFrame:
    pass

def get_years_dict(df: pd.DataFrame) -> dict:
    """Receiving a pandas.DataFrame returns a dictionary with years as keys
    and the equivalent subset of the DataFrame as values."""
    pass

def clean_dataframe(df: pd.DataFrame, drop_cols: list) -> pd.DataFrame:
    """Performs the following operations:
        Drops undesired columns;
        Converts date to datetime;
        Converts values to correct type;
        @Other?
    """
    pass

def export_dataset(df: pd.DataFrame, filename="clean_ds.csv") -> None:
    """Exports to .csv the given DataFrame with the given name"""
    pass
