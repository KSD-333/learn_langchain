import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
load_dotenv()


@tool("convert_currency", return_direct=True)
def convert_currency(query: str) -> str:
    """
    Converts currency based on a text query.
    Example input: "Convert 100 USD to INR"
    """
    try:
        parts = query.upper().split()
        
        amount = float(parts[1])
        from_currency = parts[2]
        to_currency = parts[4]

        url = f"https://v6.exchangerate-api.com/v6/50582adf7c41e3e9908c0dca/latest/{from_currency}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("result") != "success":
            return f"⚠️ API error: {data.get('error-type', 'unknown')}"

        rates = data.get("conversion_rates", {})
        if to_currency not in rates:
            return f"❌ Unsupported currency: {to_currency}"

        rate = rates[to_currency]
        converted = amount * rate
        return f"💱 {amount} {from_currency} = {converted:.2f} {to_currency} (Rate: {rate:.4f})"

    except Exception as e:
        return f"⚠️ Error: {str(e)}"



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0)

agent = initialize_agent(
    tools=[convert_currency],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

query = "Convert 100 USD to INR"
print("🪙 Query:", query)

result = agent.invoke({"input": query})
print("\n✅ Final Result:", result["output"])
