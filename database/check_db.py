import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

tables = [
    "departments",
    "employees",
    "projects",
    "employee_projects"
]

for table in tables:
    print(f"\n{'='*50}")
    print(f"TABLE: {table.upper()}")
    print("="*50)

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

conn.close()