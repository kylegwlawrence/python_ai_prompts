"""
Simple orchestrator for the ETL pipeline.
"""

from src import extract, transform, load


def run_pipeline(api_url: str, db_connection: str, table_name: str) -> None:
    """
    Run the ETL pipeline.
    """
    data = extract.fetch_data(api_url)
    if not data:
        print("Pipeline stopped: No data extracted.")
        return

    df = transform.transform_data(data)
    if df.empty:
        print("Pipeline stopped: Data transformation failed.")
        return

    load.load_data(df, db_connection, table_name)
    print("Pipeline executed successfully.")


if __name__ == "__main__":
    run_pipeline(
        api_url="https://jsonplaceholder.typicode.com/todos/1",
        db_connection="sqlite:///:memory:",
        table_name="test_table"
    )
