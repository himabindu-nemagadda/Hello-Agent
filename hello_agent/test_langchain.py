import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Add OPENROUTER_API_KEY to your .env file before running this script.")

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

response = model.invoke("What is an AI agent? Answer in one sentence.")
print(response.content)