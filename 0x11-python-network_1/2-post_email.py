#!/usr/bin/python3
""" cript that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    _, url, email = sys.argv
    params = {
        'email': email
    }
    data = urllib.parse.urlencode(params).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        r = response.read()
    print(str(r, "UTF-8"))
