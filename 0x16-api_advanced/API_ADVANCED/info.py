#!/usr/bin/python3

import requests


CLIENT_ID = "Z_Xe3TwuaNQaZ4JX-PFPKA"
SECRET_KEY = "nDQ3xPD19zaAcepZwPYhRNniZYYPdQ"

# request for an authorization token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# Initializing a dictionary
data = {
        'grant_type': 'password',
        'username': 'Aceybon',
        'password': 'Barbelieber'
        }
