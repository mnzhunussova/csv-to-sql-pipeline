# CSV to SQL Pipeline

This project demonstrates how to load a CSV file into a SQLite database and run basic SQL queries using Python.

## Files

- `data.csv` - Sample employee dataset
- `etl_script.py` - Python script to create the database, insert data, and run SQL queries

## Tools Used

- Python
- Pandas
- SQLite (via sqlite3)

## Features

- Load CSV data with pandas
- Create SQLite table and insert data
- Query all employees
- Calculate average salary by department

## How to Run

```bash
python etl_script.py
```

The script will display query results in the terminal.
