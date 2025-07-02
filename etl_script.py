
import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# Connect to SQLite (создаст базу в памяти)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

# Insert data
df.to_sql("employees", conn, if_exists="replace", index=False)

# Run SQL queries
print("All Employees:")
for row in cursor.execute("SELECT * FROM employees"):
    print(row)

print("\nAverage salary by department:")
for row in cursor.execute("""
    SELECT department, AVG(salary)
    FROM employees
    GROUP BY department
"""):
    print(row)

# Close connection
conn.close()
