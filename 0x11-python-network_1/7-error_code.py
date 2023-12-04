#!/usr/bin/python3
""" script that fetches URL content or display Error code"""

import requests
from requests import HTTPError
import sys

if __name__ == "__main__":
    _, url = sys.argv
    res = requests.request('GET', url)
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
