#!/usr/bin/python3
""" sends a request to the URL and displays the
value of the X-Request-Id variable found in the
header of the response."""
import urllib.request
import sys

if __name__ == "__main__":
    _, url = sys.argv
    with urllib.request.urlopen(url) as response:
        r_header = response.info()
    print(r_header.get('X-Request-Id'))
