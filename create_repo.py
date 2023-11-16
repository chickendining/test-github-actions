import requests
import json
import os

# Your GitHub API token
token = os.environ.get("TOKEN")
name = os.environ.get("NAME")

# Repository details
repo_name = f"A NewRepository created by {name}"
repo_description = "This is a test repo"

# GitHub API URL for creating a repository
url = "https://api.github.com/user/repos"

# Headers
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Data
data = {
    "name": repo_name,
    "description": repo_description,
    "private": False  # Set to True if you want a private repository
}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 201:
    print(f"Successfully created repository '{repo_name}'")
    print("Repository URL:", response.json()['html_url'])
else:
    print("Failed to create repository")
    print("Response:", response.content)
