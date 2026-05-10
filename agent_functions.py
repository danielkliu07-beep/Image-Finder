from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def produce_keyword(user_input):

    keyword_decider_template = """
    The user wants to find an image of the specified input. 
    Your job is to decide on a keyword that, when inputted into a search bar on an image database, will result in an image that matches what the user wants.
    Make sure the keyword either forms a sentence or a phrase
    Ex: 'Cat by the window' or 'A cat sleeps next to a window'
    Make sure the sentence grammatically makes sense. 
    Do not have a bunch of words next to eachother that doesn't flow into a sentence or a phrase.

    Here's the user input: {user_input}

    The keyword will be at least 1 word and at most 10 words. Please only include the keyword and nothing else.

    """

    model = OllamaLLM(model = "qwen3:0.6b")
    prompt = ChatPromptTemplate.from_template(keyword_decider_template)
    chain = prompt | model #creates a chain of operations using langchain (prompt is passed into model)

    result = chain.invoke({"user_input": user_input})

    return result

def evaluate_image(user_input, image_url):

    image_evaluator_template = """
    You are an image analyzer that analyzes an image and determines if the following image closely matches the user input.

    Answer 'YES' if you feel like the image closely resembles or matches the user input.
    Answer 'NO' if it doesn't resemble or match the image.
    Answer 'NO' if there are errors associated with the image like it not appearing at all.

    You should only answer 'YES' or 'NO'. Do not answer with any other response. If there's any sort of error, answer 'NO'.


    """

    model = OllamaLLM(model = "qwen3:0.6b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", image_evaluator_template),
        ("human", [
            {"type": "image_url", "image_url": {"url": "{image_url}"}},
            {"type": "text", "text": "{user_input}"}
        ])
    ])

    chain = prompt | model

    response = chain.invoke({
        "image_url": image_url,
        "user_input": user_input
    })

    return response


    













