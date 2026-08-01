import sqlite3

# Database se connect (agar file nahi hai to automatically create ho jayegi)
conn = sqlite3.connect("company.db")

# Cursor object
cursor = conn.cursor()

# -----------------------------
# Create Departments Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
)
""")

# -----------------------------
# Create Employees Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    age INTEGER,
    department_id INTEGER,
    salary REAL,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
)
""")

# -----------------------------
# Create Projects Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
)
""")

# -----------------------------
# Create Employee_Projects Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INTEGER,
    project_id INTEGER,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),
    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
)
""")

# -----------------------------
# Insert Departments
# -----------------------------
cursor.executemany("""
INSERT OR IGNORE INTO departments
(department_id, department_name)
VALUES (?, ?)
""", [
    (1, "AI"),
    (2, "HR"),
    (3, "IT"),
    (4, "Finance")
])

# -----------------------------
# Insert Employees
# -----------------------------
cursor.executemany("""
INSERT OR IGNORE INTO employees
(employee_id, employee_name, age, department_id, salary)
VALUES (?, ?, ?, ?, ?)
""", [
    (101, "Anurag", 22, 1, 80000),
    (102, "Rahul", 24, 3, 70000),
    (103, "Amit", 25, 2, 50000),
    (104, "Sneha", 23, 1, 90000),
    (105, "Priya", 26, 4, 65000)
])

# -----------------------------
# Insert Projects
# -----------------------------
cursor.executemany("""
INSERT OR IGNORE INTO projects
(project_id, project_name, department_id)
VALUES (?, ?, ?)
""", [
    (1, "Chatbot", 1),
    (2, "Payroll System", 2),
    (3, "Inventory", 3),
    (4, "Budget Planner", 4)
])

# -----------------------------
# Insert Employee Projects
# -----------------------------
cursor.executemany("""
INSERT OR IGNORE INTO employee_projects
(employee_id, project_id)
VALUES (?, ?)
""", [
    (101, 1),
    (102, 3),
    (103, 2),
    (104, 1),
    (105, 4)
])

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and tables created successfully!")