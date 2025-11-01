# AI prompt template

This is a sample AI prompt that uses an example folder structure, simple python files to demonstrate rules, and a YAML file readable by AI to define how to handle the project. 

# Example use case
This is a simple modular ETL pipeline in Python. Swap out for your own code. 

## Structure

- src/extract.py - Fetch data from an API
- src/transform.py - Transform data into a DataFrame
- src/load.py - Load data into a database
- src/main.py - Run the pipeline
- tests/ - Unit and integration tests

## Run Pipeline

```python3 -m src.main```

## Run tests
```python3 -m unittest discover tests```

