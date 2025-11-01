"""
Data loading module.
"""

import pandas as pd
from sqlalchemy import create_engine


def load_data(df: pd.DataFrame, db_connection: str, table_name: str) -> None:
    """
    Load data into a database table.

    Args:
        df (pd.DataFrame): Data to load.
        db_connection (str): Database connection string.
        table_name (str): Table name to load data into.
    """
    try:
        engine = create_engine(db_connection)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"Data loaded into table '{table_name}'.")
    except Exception as e:
        print(f"Error loading data into database: {e}")
