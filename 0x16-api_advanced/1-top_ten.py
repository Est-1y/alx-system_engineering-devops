#!/usr/bin/python3

"""
Titles of the first 10 hot posts listed.
"""

from requests import get


def top_ten(subreddit):
    """
    querying reddit api.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for index in my_data:
            print(index.get('data').get('title'))

    except Exception:
        print("None")
