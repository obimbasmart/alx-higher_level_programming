#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

import requests
import sys

if __name__ == "__main__":
    _, username, repo = sys.argv
    api_url = f'https://api.github.com/repos/{username}/{repo}/commits'
    headers = {
        'Accept': 'application/vnd.github+json',
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        res = response.json()
        for i, commit in enumerate(res):
            print(commit['commit']['tree']['sha'] + ':',
                  commit['commit']['author']['name'])
            if i == 10:
                break
    else:
        print(None)
