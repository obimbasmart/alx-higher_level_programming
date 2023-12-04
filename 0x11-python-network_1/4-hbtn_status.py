#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
html = response.text

print("Body response:\n\t- type: {}\n\t- content: {}"
      .format(type(html), html
              ))
