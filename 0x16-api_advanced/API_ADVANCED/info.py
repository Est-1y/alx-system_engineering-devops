#!/usr/bin/python3

import requests


CLIENT_ID = "5BXUX6gOYQJ8GzmvXZ6uUw"
SECRET_KEY = "Ic6OkjkdCEJ52Wp4DQuxUluKczP2Bg"

# request a temporary auth token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# Log in
# Initialize a dictionary that specifies that we are going to be login in via a password

data = {
        'grant_type': 'password',
        'username': 'alicia makena',
        'password': '1010ilovelucibel'
        }
