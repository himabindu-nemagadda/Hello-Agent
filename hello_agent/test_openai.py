import os  # Provides access to environment variables.

from dotenv import load_dotenv  # Loads variables from the .env file.
from openai import OpenAI  # Provides the OpenAI API client.

load_dotenv()  # Reads .env and makes its variables available to Python.
api_key = os.getenv("OPENROUTER_API_KEY")  # Retrieves the key without printing it.

try:  # Attempts to connect and handles any errors below.
	if not api_key:  # Checks whether the key was loaded.
		raise ValueError("OPENROUTER_API_KEY was not found in the .env file.")

	client = OpenAI(
		api_key=api_key,
		base_url="https://openrouter.ai/api/v1",
	)  # Initializes the OpenRouter-compatible client.
	client.models.list()  # Lists models to verify that the API is reachable.
	print("Connection successful!")  # Confirms success without exposing the key.
except Exception:  # Handles configuration, network, or API errors.
	print("Connection failed. Check your .env file, OpenRouter API key, and network.")

