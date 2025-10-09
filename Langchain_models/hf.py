
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint


load_dotenv()
# HF_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Define prompt
prompt = "What is the capital of India?"


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B",          
    task="text-generation",   
    # huggingfacehub_api_token=HF_API_TOKEN,
    max_new_tokens=100,
    temperature=0.7
)


response = llm.invoke(prompt)
print(response)




'''
i get so many errors when i run this code so if you are beginer chake repo_id like Inference Providers is valid or not then you will get ans other vise it is not working
'''

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

