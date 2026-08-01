from llm.model import get_llm

llm = get_llm()

def explain_result(question, dataframe):

    prompt = f"""
You are a helpful AI assistant.

User Question:
{question}

SQL Result:
{dataframe.to_string(index=False)}

Give a short and clear answer in plain English.
"""

    response = llm.invoke(prompt)

    return response.content