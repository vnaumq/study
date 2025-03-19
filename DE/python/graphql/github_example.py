import requests
import json

GITHUB_TOKEN = ''

URL = 'https://api.github.com/graphql'

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

query = """
query {
  user(login: "vnaumq") {
    name
    bio
    repositories(first: 1) {
      nodes {
        name
        description
        stargazerCount
        updatedAt
      }
    }
  }
}
"""

payload = {
    "query": query
}

response = requests.post(URL, headers=headers, json=payload)
print(response.text)
if response.status_code == 200:
    data = response.json()
    print(data)