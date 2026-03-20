from langchain_ollama import OllamaLLM

model = OllamaLLM(model = "qwen3")

result = model.invoke(input = "Hello World")
print(result)