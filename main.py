import agent_functions as agent

def start_program():
    print("Welcome to the AI Agent Finder.")
    print("Please describe what image you want to make")
    
    user_input = input()
    result = agent.produce_keyword(user_input)
    print(result)





if __name__ == "__main__":
    start_program()
