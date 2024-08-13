#!/usr/bin/python3

import json
import requests

USERNAME = 'Aceybon'
CLIENT_ID = "Z_Xe3TwuaNQaZ4JX-PFPKA"
SECRET = "nDQ3xPD19zaAcepZwPYhRNniZYYPdQ"
PASSWORD = 'Barbelieber'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)


data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD
        }

headers = {'User-Agent': 'MyRedditApp/0.1 by Aceybon'}

# Send POST request to Reddit's OAuth2 token endpoint
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

#response = response.json()

if response.status_code != 200:
    print("Failed to aunthenticate", response.status_code, response.text)
    exit()

response = response.json()

token = response.get('access_token')
#print(token)
#print(response)

# we must add the token to our haeaders whenever we are using the Reddit API.
headers['Authorization'] = f'bearer {token}'

#print(headers)
# for ex to get my identity:
identity = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

if identity.status_code == 200:
    identity = identity.json()
    #print(json.dumps(identity, indent=2))

# retrieve the most popular posts in a subreddit
hot = requests.get('https://oauth.reddit.com/r/python/hot?limit=10', headers=headers)
hot = hot.json()
#print(json.dumps(hot, indent=4))
for post in hot.get('data').get('children'):
    print(post.get('data').get('title'))
