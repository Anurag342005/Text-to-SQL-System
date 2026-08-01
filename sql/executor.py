import sqlite3
import pandas as pd


import sqlite3
import pandas as pd


def execute_sql(query):

    try:

        conn = sqlite3.connect("company.db")

        cursor = conn.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        conn.close()

        return {
            "success": True,
            "data": pd.DataFrame(rows, columns=columns),
            "error": None
        }

    except Exception as e:

        return {
            "success": False,
            "data": None,
            "error": str(e)
        }
    
if __name__ == "__main__":

    sql = "SELECT * FROM employees"

    df = execute_sql(sql)

    print(df)