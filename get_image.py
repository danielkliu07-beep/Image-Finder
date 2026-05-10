import requests

def get_unsplash_url(image_description, access_key):
    url = "https://api.unsplash.com/photos/random"

    params = {
        "query": image_description,
        "client_id": access_key
    }

    try:
        response = requests.get(url, params = params)
        response.raise_for_status() #Checks for HTTP errors

        data = response.json()
        
        return data['urls']['regular']
    
    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"
    except KeyError:
        return "Error: Couldn't find URL"