#!/usr/bin/python3

"""
timeout=0.01
print(req.status_code)
"""

import requests

req = requests.get('https://github.com', timeout=5)
print(req.status_code)
