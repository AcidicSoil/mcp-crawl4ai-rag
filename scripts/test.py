from openai import ChatCompletion
from pydantic_ai import OpenAIModel

response = ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)

model = OpenAIModel()
result = model.infer("What's the capital of France?")
print(result)