import agent_functions as agent
import scraping as scraper

def start_program():
    print("Welcome to the AI Agent Finder.")
    print("Please describe what image you want to make")
    
    user_input = input()
    agent_prompt = agent.produce_keyword(user_input)
    print(agent_prompt)
    #scraper.scrape_page_for_image(agent_prompt)
                                  


if __name__ == "__main__":
    start_program()
