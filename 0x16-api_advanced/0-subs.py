#!/usr/bin/python3
"""Returning the number of subscribers on a given subreddit
And 0 if invalid
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries.
    """

   if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
