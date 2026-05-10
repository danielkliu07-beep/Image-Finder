import agent_functions as agent
from get_image import get_unsplash_url
import base64

def start_program():
    print("Welcome to the AI Agent Finder.")
    print("Please describe what image you want to make")
    
    user_input = input()
    keyword = agent.produce_keyword(user_input)
    print(keyword)

    round = 1
    visited_urls = set()
    found_good_image = False

    while (round <= 5):
        print(f"Current iteration: {round}")
        image_url = get_unsplash_url(keyword, "frijscSLMdItFA1ef1falftsVtrMU9Un_DNjw_OakIs")
        
        print(image_url)
    
        if image_url in visited_urls:
            continue
        visited_urls.add(image_url)


        response = agent.evaluate_image(user_input, image_url)

        if (response.strip().upper() == "YES"):
            print(image_url)
            found_good_image = True
            break

        
        round += 1
    
    if (found_good_image == False):
        print("No good image was found")


if __name__ == "__main__":
    start_program()
