from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Review(BaseModel):
    summary: str = Field(description="A brief 1-2 sentence summary of the review")
    sentiment: str = Field(description="The sentiment of the review (positive, negative, or neutral)")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("I was really disappointed with this product. The quality feels cheap, and it stopped working properly after just a few days of use. The customer service was unhelpful and took too long to respond. Overall, it was a frustrating experience and definitely not worth the money.")
print("Structured Response:")
print(response)