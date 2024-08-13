#!/usr/bin/python3

import requests

"""
servers response headers.
"""
req = requests.get('https://httpbin.org/get')

print(req.headers)
"""

"""

print(req.headers['CONTENT-TYPE'])
print(req.headers.get('content-type'))

"""

"""
