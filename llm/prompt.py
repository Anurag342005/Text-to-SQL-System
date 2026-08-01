def get_prompt(schema, question):

    prompt = f"""
You are an expert SQL developer.

Your task is to convert the user's question into a valid SQLite SQL query.

Rules:
1. Return ONLY SQL.
2. Do not explain anything.
3. Do not use markdown.
4. Use only the tables and columns provided.
5. If joins are required, generate correct JOIN queries.

Database Schema:

{schema}

User Question:
{question}

SQL:
"""

    return prompt