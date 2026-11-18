import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found!")

# Create OpenAI client
client = OpenAI(api_key=api_key)


# Send prompt to the model
response = client.responses.create(
    model="gpt-5.5",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Display response
print("\nLLM Response:")
print(response.output_text)
