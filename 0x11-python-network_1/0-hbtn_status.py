#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()

print("Bad response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
      .format(type(html), html, str(html, 'UTF-8')
              ))
