#!/usr/bin/python3

"""
"""

import requests

req = requests.get('http://github.com')

print(req.url)

print(req.status_code)

print(req.history[0])

"""

"""

req = requests.get('http://github.com', allow_redirects=False)

print(req.status_code)

print(req.history)

"""

"""
req = requests.get('http://github.com', allow_redirects=False)
print(req.status_code)

req = requests.head('http://github.com')
print(req.status_code)

req = requests.head('http://github.com', allow_redirects=True)
print(req.status_code)
print(req.url)
print(req.history)
