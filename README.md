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

## Cloning this repo
Steps for cloning this repo and removing history to start with a clean slate

1. Clone the directory

```git clone https://github.com/kylegwlawrence/python_ai_prompts.git```

2. remove the git directory

```rm -rf .git```

3. init new git repo, add content, and commit

```git init && git add . && git commit -m "first commit```

4. add remote for destination repo

```git remote add origin <destination_repo_url>```

5. push new repo to empty remote

```git push -u origin master```

