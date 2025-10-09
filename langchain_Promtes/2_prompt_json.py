from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

st.header("🌏 Country Info with Gemini-2.0-flash-exp")

country = st.text_input("Ask me anything about any country")


model = GoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=api_key)

template = load_prompt("country_prompt.json")


if country and st.button("Generate"):
        prompt = template.format(country=country)
        response = model.invoke(prompt) 
        st.write(response)
    