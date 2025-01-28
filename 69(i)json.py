import requests

websitelink = "https://raw.githubusercontent.com/RaiPadam/Python-learning/refs/heads/main/names.txt"

try:
    resp = requests.get(websitelink)
    resp.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    
    # Parse JSON response
    convert_to_dict = resp.json()

    # Check if the data is a list
    if isinstance(convert_to_dict, list):
        for data in convert_to_dict:
            # Check if 'text' key exists
            if 'text' in data:
                print(data['text'])
            else:
                print("Key 'text' not found in data:", data)
    else:
        print("The JSON is not a list:", convert_to_dict)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")