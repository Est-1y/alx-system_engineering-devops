#!/usr/bin/python3

"""
"""
import json
import requests

data = {'key1': 'value1', 'key2': 'value2'}

"""
"""

ttuples = [('key3', 'value3'), ('key3', 'value4')]

ddict = {'key3': ['value3', 'value4']}



r = requests.post('https://httpbin.org/post', data=data)
#print(r.text)

r1 = requests.post('https://httpbin.org/post', data=ttuples)
#print(r1.text)

r2 = requests.post('https://httpbin.org/post', data=ddict)
#print(r2.text)
#print(r1.text == r2.text)

"""

"""

url = 'https://httpbin.org/post'
url2 = 'https://api.github.com/events'
dataa = {'some': 'dict'}
d = 'my_data'

#res = requests.post(url, data=d)
h = {'Content-Type': 'application/json'}
ress = requests.post(url2, json.dumps(dataa), headers=h)
#print(ress.json())
"""

"""

res2 = requests.post(url, json=dataa)
#print(res2.json())
#print(res.text)

"""
uploading/posting multipart encoded files
"""
#file = {'file': open('/bin/netstat', 'rb')}
#f = requests.post(url, files=file)
#print(f.text)

"""
Set the filename, content_type and headers
"""
#files = {'file': ('netstat', open('/bin/netstat', 'rb'), {'Expires': 0})}
#f = requests.post(url, files=files)
#print(f.text)

"""
If you want you can send strings to be received as files.

"""
f = {'file': ('my_file.txt', 'My name is Acey\nI am from Carolina.\nI came here in 2019\n')}
response = requests.post(url, files=f)
print(response.text)
