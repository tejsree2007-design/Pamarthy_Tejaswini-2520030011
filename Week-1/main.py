
import ollama

response = ollama.generate(
    model="llama3.2",
    prompt="What is Artificial Intelligence?"
)

print(response["response"])
