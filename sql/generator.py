from llm.model import get_llm
from llm.prompt import get_prompt
from utils.schema import get_schema


llm = get_llm()


def generate_sql(question):

    schema = get_schema()

    prompt = get_prompt(schema, question)

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    question = "Show all employees."

    sql = generate_sql(question)

    print(sql)