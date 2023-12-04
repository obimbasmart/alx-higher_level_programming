#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

_, url = sys.argv
with urllib.request.urlopen(url) as response:
    r_header = response.info()

print(r_header.get('X-Request-Id'))
