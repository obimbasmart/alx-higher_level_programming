#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": ""}
    if len(sys.argv) > 1:
        params["q"] = sys.argv[1]
    res = requests.request('POST', url, data=params)

    try:
        if not len(res.json()):
            print("No result")
        else:
            print("[{}] {}".format(res.json()['id'], res.json()['name']))
    except Exception as e:
        print("Not a valid JSON")
