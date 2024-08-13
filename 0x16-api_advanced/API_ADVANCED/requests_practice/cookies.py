#!/usr/bin/python3

"""
If response from server contains some cookies, you can access them
"""

import requests


r = requests.get('https://httpbin.org/get')

url = 'https://httpbin.org/cookies'
cookies = {'cookies-are': 'working', 'cookies-allowed': 'True'}

res = requests.get(url, cookies=cookies)
print(res.text)

cookie_jar = requests.cookies.RequestsCookieJar()

cookie_jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
cookie_jar.set('gross_cookie', 'yuck', domain='httpbin.org', path='/elsewhere')

url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=cookie_jar)
print(r.text)
