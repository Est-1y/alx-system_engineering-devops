#!/usr/bin/python3

"""
If the response from the server contains some cookies, you can access them.
"""

import requests


r = requests.get('https://httpbin.org/get')

#print(r.text)
#print(r.headers)
#print(r.cookies.get('example_cookie_name', None))

# To send your own cookies to the server, you can use the cookies param.

url = 'https://httpbin.org/cookies'
cookies = {'cookies-are': 'working', 'cookies-allowed': 'True'}

res = requests.get(url, cookies=cookies)
print(res.text)

# Cookies are returned in a RequestsCookieJar:
# This acts like a dict but provides a more complete interface,
# suitable for use over multiple domains or paths

# Cookie jars can also be passed in to requests...
cookie_jar = requests.cookies.RequestsCookieJar()

cookie_jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
cookie_jar.set('gross_cookie', 'yuck', domain='httpbin.org', path='/elsewhere')

url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=cookie_jar)
print(r.text)
