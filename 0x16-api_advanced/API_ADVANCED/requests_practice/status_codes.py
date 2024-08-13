#!/usr/bin/python3


import requests

url = 'https://httpbin.org/get'
req = requests.get(url)


# print(req.status_code == requests.codes.ok)

"""

"""
bad = requests.get('https://httpbin.org/status/404')
# print(bad.status_code)


print(req.raise_for_status())
