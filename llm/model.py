import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Read API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Create LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=groq_api_key
)


def get_llm():
    return llm


# Testing
if __name__ == "__main__":

    llm = get_llm()

    response = llm.invoke("Who are you?")

    print(response.content)