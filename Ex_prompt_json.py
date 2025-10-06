from langchain.prompts import PromptTemplate


template = PromptTemplate(
    template="""
    What is the capital of {country}? and provide some information about it.
    eg(how many people live there, famous places to visit etc.)
    """,
    input_variables=["country"],
    validate_template=True
)

template.save("country_prompt.json")