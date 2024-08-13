#!/usr/bin/python3

import json
import requests
from PIL import Image
from io import BytesIO


# try to get a web page
# For this example, let’s get GitHub’s public timeline:

response = requests.get('https://api.github.com/events')

# We now have a response object called response.
# get all the infor we need from this object.

#print(response.json())
#print(response.status_code)

# How to make HTTP Post request
response2 = requests.post('https://httpbin.org/post', data={'key': 'value'})

#print(response2.status_code)
#print(response2.json())

response3 = requests.put('https://httpbin.org/put', data={'name': 'bon'})
#print(response3.json())

response4 = requests.delete('https://httpbin.org/delete')
#print(response4.json())
#print(response3.status_code)

response5 = requests.head('https://httpbin.org/get')
#print(response5.headers)

response6 = requests.options('https://httpbin.org/get')
#print(response6.headers)


# PASSING PARAMETERS IN URLS
# We might want to send some data in the URL's query string
# If we were constructing the URL by hand, we would add this data in the query string of the URL aas key,value pairs after the ?
# for ex: https://httpbin.org/get?name=Esther

# Requests allows you to provide these arguments as a dict of strings;
# using the params keyword argument.

data = {'name': 'Ace', 'age': 20}

r = requests.get('https://httpbin.org/get', params=data)

# you can see that the url has been correctly encoded by printing it:
#print(r.url) # https://httpbin.org/get?name=Ace&age=20

# Any dictionary key whose value is None will not be added to the URL query string
my_data = {'color': 'blue', 'material': 1000, 'origin': None}
r1 = requests.put('https://httpbin.org/put', params=my_data)
#print(r1.url)

# You can pass a list of items as a value 
my_dict = {'Drinks': ['Water', 'Juice'], 'destination': 'Nakuru'}
r2 = requests.post('https://httpbin.org/post', params=my_dict)
#print(r2.url) # https://httpbin.org/post?drinks=water&drinks=juice&destination=Nakuru

r3 = requests.get('https://www.reddit.com/r/gaming/about.json')
data = r3.json().get('data')
#subs = data.get('subscribers')
#print(subs)

# RESPONSE CONTENT
# We can read content of server's response:

r4 = requests.get('https://api.github.com/events')
#print(r4.text)
#print(r4.encoding)
r4.encoding = 'ISO-8859-1'
#print(r4.encoding)
# Requests automatically decodes content from the server.
# You can find out what encoding Requests is using, and change it,
# using the encoding property.

# For non text requests, you can access the request body as bytes
car = requests.get('https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')

#print(car.content)
# To create an image from binary data returned from a request
my_car = Image.open(BytesIO(car.content))
#my_car.show()

# JSON RESPONSE CONTENT:
"""
requests has a builtin json decoder-> in case you are dealing with json data.
"""
timeline = requests.get('https://api.github.com')
print(timeline.raise_for_status())
try:
    obj = json.loads(timeline)
    print(obj)
except Exception as e:
    #print("Unsuccessful decoding")
    pass
#print(timeline.text)
timeline = timeline.json()

"""
if the json decoding fails, timeline.json() will raise an exception.

For ex if the response gets a 204(No Content),
or the response contains invalid json.
    => requests.exceptions.JSONDecodeError

NB:
    The success of the call to json() does not indicate the success of the response.
    This is because some servers might return a JSON object in a failed response eg error details with HTTP 500.
    So this JSON will be decoded and returned.

    To check the success of a request, use response.status_code or response.raise_for_status()
"""

#print(timeline)
#print(type(timeline))

# To get the raw socket response from the server, you can use the raw property.
# If you want to do this, make sure you set stream=True in the initial request.

header = {'Accept-Encoding': 'Identity'}
r = requests.get('https://api.github.com/events', stream=True, headers=header)

#print(r.raw.read(10))

# it is best however to use a pattern like this to save what is being streamed to a file.
# Another way is to ask the server not to send the response in gzip format. You can do this by setting the Accept-Encoding header to identity, which tells the server to send the response without any content encoding.

with open('my_response.txt', 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        if chunk:
            f.write(chunk)
