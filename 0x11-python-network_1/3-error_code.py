#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response """
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    _, url = sys.argv

    try:
        with urllib.request.urlopen(url) as response:
            res = response.read()
    except HTTPError as err:
        print("Error code ", err.code)
    else:
        print(str(res, "UTF-8"))
