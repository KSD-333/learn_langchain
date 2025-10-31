import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env if present
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Missing GROQ_API_KEY. Set it in your environment or .env file.")

# Allow model override via env; keep a sensible default
model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

client = Groq(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Explain the importance of fast language models"}
    ],
    model=model,
)

print(chat_completion.choices[0].message.content)