from sql.generator import generate_sql
from sql.executor import execute_sql


def main():

    question = input("Ask your question: ")

    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)

    result = execute_sql(sql)

    print("\nResult:")

    for row in result:
        print(row)


if __name__ == "__main__":
    main()