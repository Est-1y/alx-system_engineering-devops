#!/usr/bin/python3
"""
number of subscribers for a reddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ querying subscriber count"""
    if subreddit and type(subreddit) is str:
        subscribers = 0
        url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        request = get(url, headers=headers)
        if request.status_code == 200:
            data = request.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
