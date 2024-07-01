
import requests
from munch import Munch

def test_get_workflow():
    
    # Define the necessary variables
    GITHUB_TOKEN = 'your token'
    OWNER = 'fazleyazdan7'
    REPO = 'github-api'
    WORKFLOW_ID = 'main.yml' 

    # end point
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}"

    # Headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    # Make a request
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    workflow_info = Munch(response.json())
    
    assert workflow_info.name == "hello-world"
    assert workflow_info.state == "active"
    
    # Check the response status and print the workflow information
    # if response.status_code == 200:
    #     workflow_info = response.json()
    #     print(workflow_info)
    # else:
    #     print(f"Failed to retrieve workflow information: {response.status_code}")
    #     print(response.json())

