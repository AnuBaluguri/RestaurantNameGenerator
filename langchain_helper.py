import os
# Import ChatGroq from the new langchain_groq package
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain

# Set Groq API Key
os.environ["GROQ_API_KEY"] = "Paste_your_Groq_API_KEY"

# Initialize ChatGroq
llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama3-8b-8192"
)

def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name for this with no explanation. Give only name as output, no extra lines",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 10 menu items for {restaurant_name}. Return only a comma-separated list with no explanation or extra lines.",
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    

    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ["cuisine"],
    output_variables = ["restaurant_name", "menu_items"]
    )

    response = chain({'cuisine': cuisine})
    
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
