from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI(
    base_url="http://127.0.0.1:8000/guards/gibberish_guard/openai/v1",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hi!",
        },
    ],
)

print(response.choices[0].message.content)
print(response.guardrails["validation_passed"])
