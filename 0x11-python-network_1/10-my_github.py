#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys


if __name__ == "__main__":
    _, username, access_token = sys.argv
    api_url = 'https://api.github.com/user'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print(response.json().get('id'))
