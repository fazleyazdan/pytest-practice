import requests

def get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError


