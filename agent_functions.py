from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


keyword_decider_template = """
The user wants to find an image of the specified input. 
Your job is to decide on a keyword that, when inputted into a search bar on an image database, will result in an image that matches what the user wants.

Here are the past suggestions: {context}

Here's the user input: {user_input}

The keyword will be at least 1 word and at most 10 words. Please only include the keyword and nothing else.

"""

model = OllamaLLM(model = "qwen3:0.6b")
prompt = ChatPromptTemplate.from_template(keyword_decider_template)
chain = prompt | model #creates a chain of operations using langchain (prompt is passed into model)


def produce_keyword(user_input):
    context = ""
    result = chain.invoke({"context": context, "user_input": user_input})

    context = context + f"\nAI: {result}"

    return result




