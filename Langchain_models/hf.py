from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage

# Load .env
load_dotenv()

# Get HF token (ensure no quotes around the token)
hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN").strip()

# Create HuggingFaceEndpoint with explicit token
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",  # public model
    huggingfacehub_api_token=hf_token,
    task="text-generation",
    temperature=0.7,
    max_new_tokens=200
)


# Wrap in ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# Send prompt
result = model.invoke([HumanMessage(content="What is the capital of India?")])

print(result.content)
