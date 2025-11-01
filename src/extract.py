"""
Data extraction module.
"""

import requests
from typing import Dict, Any


def fetch_data(api_url: str) -> Dict[str, Any]:
    """
    Fetch data from an API endpoint.

    Args:
        api_url (str): URL of the API endpoint.

    Returns:
        Dict[str, Any]: Data fetched from the API.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return {}