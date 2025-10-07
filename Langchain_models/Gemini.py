# from google import genai

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)

# import google.generativeai as genai

# # Configure API key
# genai.configure(api_key="AIzaSyCegRpM_fnTaaCCYwNOAd6eezijczJih9w")

# # Choose a Gemini model (e.g., gemini-1.5-flash or gemini-1.5-pro)
# model = genai.GenerativeModel("gemini-2.5-flash")

# # Generate content
# response = model.generate_content("Write a short poem about AI and creativity")

# print(response.text)


# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# response = chat.invoke("Explain how AI works in a few words")
# print(response)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # "gemini-2.5-flash" not yet public
    google_api_key=api_key
)

response = chat.invoke("is langchain is require api pass in at time of model creation?")

print(response.content)
