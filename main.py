from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model = "qwen3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model #creates a chain of operations using langchain (prompt is passed into model)

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot, Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context = context + f"\nUser: {user_input}\nAI: {result}" #stores the context into the bot


if __name__ == "__main__":
    handle_conversation()
