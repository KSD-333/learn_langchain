from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
import streamlit as st


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

st.header("🌏 Country Info with Gemini-2.0-flash-exp")

country = st.text_input("Ask me anything about any country")


model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=api_key)

template = PromptTemplate(
    template="""
    What is the capital of {country}? and provide some information about it.
    eg(how many people live there, famous places to visit etc.)
    """,
    input_variables=["country"],
    validate_template=True
)

if country and st.button("Generate"):
        prompt = template.format(country=country)
        response = model.invoke(prompt) 
        st.write(response.content)
    