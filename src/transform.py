"""
Data transformation module.
"""

import pandas as pd
from typing import Dict


def transform_data(data: Dict) -> pd.DataFrame:
    """
    Transform raw data into a pandas DataFrame.

    Args:
        data (Dict): Raw data dictionary.

    Returns:
        pd.DataFrame: Transformed data as a DataFrame.
    """
    try:
        df = pd.DataFrame([data])
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return pd.DataFrame()
