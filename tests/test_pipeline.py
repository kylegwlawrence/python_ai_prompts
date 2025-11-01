import unittest
from src import main


class TestPipeline(unittest.TestCase):
    """Integration test for the ETL pipeline."""

    def test_pipeline_runs(self):
        """Ensure the pipeline runs without errors."""
        try:
            main.run_pipeline(
                api_url="https://jsonplaceholder.typicode.com/todos/1",
                db_connection="sqlite:///:memory:",
                table_name="test_table"
            )
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
