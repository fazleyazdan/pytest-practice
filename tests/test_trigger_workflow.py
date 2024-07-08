import requests
from munch import Munch

def test_get_workflow():
    
    # Define the necessary variables
    GITHUB_TOKEN = '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'
    OWNER = 'fazleyazdan7'
    REPO = 'github-api'
    WORKFLOW_ID = 'main.yml'  

    # headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }
    
    trigger_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"

    # payload with the branch name
    data = {
        "ref": "main"  
    }

    # Make the POST request to trigger the workflow
    response = requests.post(trigger_url, headers=headers, json=data)

    # Check the response status 
    assert response.status_code == 204
    
    # if response.status_code == 204:
    #     print("Workflow triggered successfully!")
    # else:
    #     print(f"Failed to trigger workflow: {response.status_code}")
    #     print(response.json())