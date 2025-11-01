import unittest
import pandas as pd
from src import load


class TestLoad(unittest.TestCase):

    def test_load_data(self):
        df = pd.DataFrame([{"id": 1, "title": "Test"}])
        try:
            load.load_data(df, "sqlite:///:memory:", "test_table")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
