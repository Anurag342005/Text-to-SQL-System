import sqlite3

def get_schema():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)

    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        schema += f"\nTable: {table_name}\n"

        for column in columns:
            schema += f"- {column[1]} ({column[2]})\n"

    conn.close()

    return schema


if __name__ == "__main__":
    print(get_schema())