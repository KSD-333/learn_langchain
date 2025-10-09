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