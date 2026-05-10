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
    Do not have stuff like parenthesis in your final response.

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
    You are an image analyzer. Your job is to determine if an image is a reasonable match for what the user wants.

    Answer 'YES' if the image is somewhat related to the user's request and resembles the user's request.
    Answer 'NO' only if the image is completely unrelated.
    Answer 'NO' if there are errors associated with the image like it not appearing at all.

    You should only answer 'YES' or 'NO'. Do not answer with any other response.
    """

    model = OllamaLLM(model = "llava:latest")
    prompt = ChatPromptTemplate.from_messages([
        ("system", image_evaluator_template),
        ("human", [
            {"type": "text", "text": "The user wants: '{user_input}'. Does this image reasonably match that? Answer YES or NO."},
            {"type": "text", "text": "{user_input}"}
        ])
    ])

    chain = prompt | model

    response = chain.invoke({
        "image_url": image_url,
        "user_input": user_input
    })

    return response


    













